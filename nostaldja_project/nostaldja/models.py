from django.db import models

# Create your models here.


class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.name


class Fad(models.Model):
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=255)
    image_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
