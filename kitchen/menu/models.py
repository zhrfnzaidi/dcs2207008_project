from django.db import models

# Create your models here.

class Feedback(models.Model):
   name = models.TextField()
   text = models.TextField()
