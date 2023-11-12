from django.db import models
from django.db.models.fields.files import ImageField


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    pub_date = models.DateField("fecha de registro",auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    imagen = models.ImageField(upload_to='curso_images/')

    def __str__(self):
        return self.nombre