from django.db import models

# Create your models here.


class Massif(models.Model):
    massif_name = models.CharField(max_length=200)


    def __str__(self):
        return self.massif_name


class Glacier(models.Model):
    massif = models.ForeignKey(Massif, on_delete=models.CASCADE, default=1)
    glacier_name = models.CharField(max_length=200)
    glacier_length = models.FloatField(default=0)
    glacier_area = models.FloatField(default=0)


    def __str__(self):
        return self.glacier_name