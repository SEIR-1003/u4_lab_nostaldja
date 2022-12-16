from django.db import models

# Create your models here.
class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Fads(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField(null=True)
    description = models.TextField(max_length=500, null=True)
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='decade')
