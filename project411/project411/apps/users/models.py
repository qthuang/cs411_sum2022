from django.contrib.auth.models import AbstractUser
from django.db import models

# Overwrite user table provided by django
class User(AbstractUser):
    email = models.CharField(max_length=30, unique=True, verbose_name='email_address', null=True)
    password = models.CharField(max_length=30, unique=True, verbose_name='password', null=True)
    class Meta:
        db_table = "tb_user"
    def __str__(self):
        return self.username

# own user table
class ProjectUser(models.Model):
    email = models.CharField(max_length=30, unique=True, verbose_name='email_address', null=True)
    password = models.CharField(max_length=30, unique=True, verbose_name='password', null=True)


    class Meta:
        db_table = "tb_ProjectUser"
    def __str__(self):
        return self.email




