from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=900)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="imagenes")
    disponibilidad=models.BooleanField(default=True)
    precio=models.FloatField(default=0)

    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'



