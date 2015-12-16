# -- coding: utf-8 -
from django.db import models
from django.template.defaultfilters import slugify

class Cliente(models.Model):
    name = models.CharField(max_length=128, unique=True)
    #views = models.IntegerField(default=0)
    #likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cliente, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    fechaPedido = models.CharField(max_length=128)
    precio = models.CharField(max_length=128)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
