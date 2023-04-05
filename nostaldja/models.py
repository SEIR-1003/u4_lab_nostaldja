from django.db import models

# Create your models here.
class Decade(models.Model):
  name = models.CharField(max_length = 100) # eighties, nineties, etc.
  start_year = models.IntegerField()
  end_year = models.IntegerField()

  def str(self):
    return self.name

class Fads(models.Model):
  name = models.CharField(max_length = 100)
  image_url = models.TextField()
  description = models.TextField()
  decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

  def str(self):
    return self.name


