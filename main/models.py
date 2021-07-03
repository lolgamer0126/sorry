from django.db import models

# Create your models here.
class Accounts(models.Model):
    username = models.TextField()
    passwd = models.TextField()
    def __str__(self):
        return self.username
      