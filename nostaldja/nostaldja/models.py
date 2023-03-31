from django.db import models

# Create your models here.


class Decade(models.Model):
    name = models.CharField(max_length=120)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name


class Fads(models.Model):
    name = models.CharField(max_length=120)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
