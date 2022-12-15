from django.db import models

# Create your models here.
class Fads(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.CharField(max_length=150)
    decade = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Decade(models.Model):
    name = models.ForeignKey(Fads, on_delete=models.CASCADE, related_name='years')
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year