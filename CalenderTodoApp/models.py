from django.db import models


# Create your models here.
class TodoModel(models.Model):
    createuser = models.TextField()
    createdate = models.CharField(max_length=50)
    todo = models.TextField()
