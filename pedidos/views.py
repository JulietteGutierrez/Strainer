from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from publica.carrito import Carrito
from pedidos.models import LineaPedido, Pedido
from publica.models import Producto
from publica.context_processor import importe_total_carrito_centavos
import mercadopago
import environ

env = environ.Env()
environ.Env.read_env()
# Create your views here.

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carrito = Carrito(request)
    lineas_pedido = []
    total = importe_total_carrito_centavos(request)/100.
    env = environ.Env()
    environ.Env.read_env()
    token=env("ACCESS_TOKEN")
    public_key=env("PUBLIC_KEY")


    for key, value in carrito.carrito.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    productos = [linea.producto for linea in lineas_pedido]
 
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email,
        total=total
    )

    sdk = mercadopago.SDK(token)

    preference_data = {
        "items": [
            {
                "title": "Tu compra en Strainer Coffee",
                "total_amount": total,
                "currency_id": "ARS",
                "quantity": 1,
                "unit_price": total,
            }
        ],
     }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    preference_id = preference_response['response']['id']    
    productos = request.session.pop('productos', [])
      
    return render(request, "publica/realizar_pago.html", {
        "productos": productos,
        "preference": preference,
        "preference_id": preference_id,
        "nombreusuario": request.user.username,
        "valor_total": total,
        "lineas_pedido": lineas_pedido,
        "public_key": public_key
    })
    
def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),
        "email_usuario":kwargs.get("email_usuario"),
        "total":kwargs.get("total")
        })

    mensaje_texto = strip_tags(mensaje)
    #from_email="holastrainer@gmail.com" 
    from_email=env("EMAIL_HOST_USER")
    to=kwargs.get("email_usuario")
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
