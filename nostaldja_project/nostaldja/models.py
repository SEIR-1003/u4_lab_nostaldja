from django.db import models

# Create your models here.

class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100, default='fad name')
    image_url = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, default='fad description')

    def __str__(self):
        return self.name
    
