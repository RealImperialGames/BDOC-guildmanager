from django.db import models

# Create your models here.


class Guild(models.Model):

    name = models.CharField(default="UNAMMED", max_length=20)

    def __str__(self):
        """Todo: doc method"""
        return self.name
