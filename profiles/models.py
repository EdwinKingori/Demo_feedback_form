from django.db import models

# Create your models here.


class Userprofile(models.Model):
    image = models.FileField(upload_to="images")
