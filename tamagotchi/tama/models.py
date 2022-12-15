from django.db import models

# Create your models here.

class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class Fads(models.Model):
    name = models.ForeignKey(Decade, on_delete=models.CASCADE,related_name='fads') 
    image_url=models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, default='no fad description')
    decade = models.CharField(max_length=20, default='no decade entered')

    def __str__(self):
        return self.name