from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=50, blank=False)
    quantidade = models.CharField(max_length=20, blank=True)
    valor = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        return self.name