from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=40,null=True,blank=True)
    email = models.EmailField(unique=True, max_length=30)
    username = models.CharField(max_length=255, unique=False)
    phone_number = models.CharField(unique=True,max_length=15,null=False,blank=False)
    profession = models.CharField(max_length=40,null=True,blank=True)
    place = models.CharField(max_length=40,null=True,blank=True)
    is_group = models.BooleanField(default=False,null=False)
    soft_delete = models.BooleanField(default=False,null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        db_table = "User"

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, through='Group_members')

    class Meta:
        db_table = "Groups"

class Group_members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)  

    class Meta:
        db_table = "Group_Members"  