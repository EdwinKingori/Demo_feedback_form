from django.db import models

# Create your models here.


class Userprofile(models.Model):
    image = models.ImageField(upload_to="images")
