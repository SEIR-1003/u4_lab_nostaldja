from django.db import models

# Create your models here.
# tunr/models.py
class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fad')
    name = models.CharField(max_length=100, default= 'nope')
    image_url = models.TextField(max_length=200, null=True)
    description_of_it = models.TextField(max_length= 255, default='no description')


    def __str__(self):
        return self.name
