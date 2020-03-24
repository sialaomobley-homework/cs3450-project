from django.db import models
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)


class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
# Create your models here.
