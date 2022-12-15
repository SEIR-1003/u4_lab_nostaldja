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
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100, default='no fad')
    image_url = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=100, default='no description')
    decade = models.CharField(max_length=100, default='no decade')
    

    def __str__(self):
        return self.name