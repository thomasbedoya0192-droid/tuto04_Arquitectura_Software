from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)
    stock_actual = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
