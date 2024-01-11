# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)

    def __str__(self):
        return self.name
