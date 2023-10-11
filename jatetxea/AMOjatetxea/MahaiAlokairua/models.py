from django.db import models

# Create your models here.

class Mahaia(models.Model):
    zenbakia = models.CharField(max_length = 3, primary_key=True)

    def ___str___(self):
        return self.zenbakia

class Bezeroa(models.Model):
    dni = models.CharField(max_length = 10, primary_key=True)
    izena = models.CharField(max_length = 25)
    abizena = models.CharField(max_length = 25)

    def __str__(self):
        return self.izena

class Alokairua(models.Model):
    mahai_zenbakia = models.ForeignKey(Mahaia, on_delete = models.CASCADE)
    bezero_dni = models.ForeignKey(Bezeroa, on_delete = models.CASCADE)
    alokairu_data = models.DateField(null = True)
    alokairu_ordua = models.CharField(max_length = 10)