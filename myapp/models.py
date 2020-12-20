from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.title