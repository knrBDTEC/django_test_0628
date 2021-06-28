from django.db import models

# Create your models here.
class BDTEC_data(models.Model):
    BD_text = models.CharField(max_length=200)
    BD_date = models.DateTimeField('sensor data')

    def __str__(self):
        return self.BD_text