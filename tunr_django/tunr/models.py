from django.db import models

# Create your models here.
# tunr/models.py
class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=5, default='start year')
    end_year = models.CharField(max_length=5, default='end year')

    def __str__(self):
        return self.name


class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='decade')
    image_url = models.CharField(max_length=100, default='fad photo')
    fad = models.CharField(max_length=100, default='fad')
    description = models.TextField(max_length=300, default='description')

    def __str__(self):
        return self.fad

