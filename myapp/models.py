from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name



class Story(models.Model):
    title = models.CharField(max_length=300)
    body = RichTextField()
    story_image = models.ImageField(blank=True, null=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.first_name + ' ' + self.last_name
