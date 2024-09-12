from django.db import models

# Create your models here.
# tunr/models.py
class Decades(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fads(models.Model):
    name = models.ForeignKey(Decades, on_delete=models.CASCADE, related_name='fads')
    image_url = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=100, default='no description')
    decade = models.CharField(max_length=100, default='no decade')


    def __str__(self):
        return self.decade