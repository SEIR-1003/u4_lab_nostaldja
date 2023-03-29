from django.db import models

# Create your models here.
# A Decade will have Fads, or in other words a fad will have a
# foreign key for a decade.

class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete= models.CASCADE, related_name='fads' )
    name = models.CharField(max_length=100, default="no name")
    image_url = models.TextField()
    description = models.CharField(max_length=100, default="no description")

    def __str__(self):
        return self.name