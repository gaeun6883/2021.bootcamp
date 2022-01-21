from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MainContent(models.Model):
 title = models.CharField(max_length=200)
 content = models.TextField()
 pub_date = models.DateTimeField('date published')

 def __str__(self):
     return self.title


class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
