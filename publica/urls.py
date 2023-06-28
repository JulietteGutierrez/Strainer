from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='inicio'),
    path('origenes/',views.origenes,name='origenes'), 
    path('sucursales/',views.sucursales,name='sucursales'),
    path('contacto/',views.contacto,name='contacto'),  
    path('tienda/',views.tienda,name='tienda'),
    path('tienda/producto/<int:id>', views.tiendaProducto, name='producto'),
    path('tienda/comprar', views.tiendaComprar, name='comprar'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    # path('tienda-online/carrito/<int:id>/<int:cantidad>', views.tiendaCarritoAgregar, name='carrito'),
]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
