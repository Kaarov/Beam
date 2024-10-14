from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    bio = models.TextField()
