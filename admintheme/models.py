from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Instancias
class Instance(models.Model):
    User = models.ForeignKey(User)
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    token = models.CharField(max_length=32)

# Atributos de cada sitio
class Attributes(models.Model):
    Instance = models.OneToOneField(Instance)
    main_color = models.CharField(max_length=6)
    dark_color = models.CharField(max_length=6)
    light_color = models.CharField(max_length=6)
    bg_color = models.CharField(max_length=6)
    main_bg = models.CharField(max_length=6)
    secondary = models.CharField(max_length=6)
    gray = models.CharField(max_length=6)
    gray_3 = models.CharField(max_length=6)
    gray_2 = models.CharField(max_length=6)
    gray_1 = models.CharField(max_length=6)
    black = models.CharField(max_length=6)
    black_80 = models.CharField(max_length=6)
    logo_header = models.CharField(max_length=250)
    banner = models.CharField(max_length=250)

# Log de cambios
class ChangeLog(models.Model):
    Instance = models.ForeignKey(Instance)
    date_log = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

# Perfil de usuario
class UserProfile(models.Model):
    User = models.OneToOneField(User)
    avatar = models.CharField(max_length=254)