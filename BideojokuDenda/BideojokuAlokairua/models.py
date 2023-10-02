from django.db import models

# Create your models here.

class Bideojokua(models.Model):
    bid_id = models.CharField(max_length=50)
    bid_izena = models.CharField(max_length=100)
    bid_generoa = models.CharField(max_length=100)
    bid_hizkuntza = models.CharField(max_length=50)
    bid_irteeradata = models.DateField()
    bid_adinminimoa = models.IntegerField()
    bid_sinopsia = models.CharField(max_length=250)


    def __unicode__(self):
        return self.bid_izena
    
class Bezeroa(models.Model):
    bez_dni = models.CharField(max_length=20)
    bez_izena = models.CharField(max_length=30)
    bez_abizena = models.CharField(max_length=50)
    bez_telefonoa = models.CharField(max_length=20)
    bez_email = models.CharField(max_length=50)
    bez_helbidea = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.bez_izena + " " + self.bez_abizena

class Alokairua(models.Model):
    bezeroa = models.ForeignKey(Bezeroa, on_delete=models.CASCADE)
    bideojokua = models.ForeignKey(Bideojokua, on_delete=models.CASCADE)
    