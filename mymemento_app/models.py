from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Memento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # A field for creating a one-to-many relationship with another model
    published_date = models.DateField() # A field for storing a date value
    title = models.CharField(max_length=75)
    text = models.CharField(max_length=250) # A field for storing a text with a maximum length
    img = models.ImageField(upload_to='static/mementos_files/images', default='') # A field for storing an image
    audio = models.FileField(upload_to='static/mementos_files/audios', default='') # A field for storing an audio

    def __str__(self):
        return f"{self.title} - {self.user}"