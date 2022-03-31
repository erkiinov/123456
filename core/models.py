from importlib.resources import contents
from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    nomi = models.CharField(max_length=50)
    daromadi = models.IntegerField()


    def __str__(self):
        return self.nomi

class Post2(models.Model):
    name = models.CharField(max_length=50)
    profit = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name
    def __str__(self):
        return self.content

class Post3(models.Model):
    name = models.CharField(max_length=50)
    profit = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name
    def __str__(self):
        return self.content

class Post4(models.Model):
    name = models.CharField(max_length=50)
    profit = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name
    def __str__(self):
        return self.content

class Post5(models.Model):
    name = models.CharField(max_length=50)
    profit = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name
    def __str__(self):
        return self.content

class Post6(models.Model):
    name = models.CharField(max_length=50)
    profit = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name
    def __str__(self):
        return self.content
        
class Post6(models.Model):
    name = models.CharField(max_length=50)
    profit = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name
    def __str__(self):
        return self.content