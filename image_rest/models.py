from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image = models.ImageField()
    uploader = models.ForeignKey(User, related_name="uploaded_images", on_delete=models.SET_NULL, null=True)
    name = models.TextField()

