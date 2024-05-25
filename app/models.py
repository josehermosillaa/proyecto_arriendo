from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator
# Create your models here.

class Usuario(models.Model):
    """ este usuario es el que se usa para registrarse, loggearse etc auth.User"""
    #PK autofield
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Inmueble(models.Model): 
    #P
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id_tipo_inmueble = models.ForeignKey('Tipo_inmueble', on_delete=models.CASCADE)
    id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE)
    nombre_inmueble = models.CharField(max_length=200)
    m2_construido = models.FloatField()
    numero_banos = models.IntegerField(validators= [MinValueValidator(0)],default=0)
    numero_hab = models.IntegerField(validators= [MinValueValidator(0)],default=0)
    direccion = models.CharField(max_length=200)

class Region(models.Model):
    region = models.TextField()
    

class Comuna(models.Model):
    comuna = models.TextField()

class Tipo_inmueble(models.Model):
    CHOICES = [
        ('Departamento', 'Departamento'),
        ('Casa', 'Casa'),
        ('Parcela', 'Parcela'),
    ]
    tipo = models.TextField(choices=CHOICES)

    """Departamento, Casa, Parcela"""
    """
    ID  tipo
    1   Departamento
    2   Casa
    3   Parcela
    """


class Tipo_usuario(models.Model):
    """ arrendatario, arrendador  """
    CHOICES = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario')
    ]
    tipo = models.CharField(choices=CHOICES)

class Perfil(models.Model):
    usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    rut = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    correo = models.EmailField()
    
    
    
    """
    usuario = models.OneToOneField(User, ...)
    rut 
    tipo_usuario = models.OneToOneField(Tipo_usuario)
    direccion
    telefono
    correo 
    #USUARIO 
    """