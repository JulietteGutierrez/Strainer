def importe_total_carrito(request):
  # if request.user.is_authenticated:
    total=0
    # mientras terminamos la autenticacion, le ponemos un try / except para que no explote
    # despues cuando ande el if de is_authenticated volamos el try / except
    try:
        for key, value in request.session["carrito"].items():
            total=total+float(value["precio"])
    except:
        total=0

    return {"importe_total_carrito": total}
    

    # total=0    
    # if request.user.is_authenticated:
    #     for key, value in request.session["carrito"].items():
    #         total=total+float(value["precio"])
    # else:
    #     total="Debes hacer login"
           
    # return {"importe_total_carrito":total}

def importe_total_carrito_centavos(request):
    total = 0.0

    try:
        carrito = request.session.get("carrito", {})
        for key, value in carrito.items():
            cantidad = value.get("cantidad", 0)
            precio = value.get("precio", 0.0)
            subtotal = cantidad * float(precio)
            total += subtotal
    except:
        total = 0.0

    total_en_centavos = int(total * 100)  # Convertir a centavos como entero

    return total_en_centavos

