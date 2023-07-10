from datetime import date
import email
from locale import normalize
from pyexpat import model
from re import fullmatch
from select import select
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.

class Complaint(models.Model):
    name =models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=13)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Signup(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=70)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return self.fullname
    
class AccountManager(BaseUserManager):
    def create_user(self,email,username,fullname,password=None):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            fullname = fullname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,fullname, password):
        user = self.create_user(
            email=email,
            username=username,
            fullname=fullname,
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    email=models.EmailField(primary_key=True, max_length=255, verbose_name="Email")
    username= models.CharField(max_length=255,unique=True,verbose_name="Username")
    fullname=models.CharField(max_length=255,verbose_name="fullname")

    date_joined=models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'fullname']

    object = AccountManager()

    def has_perm(self,perm,obj=None):
        return  self.is_admin

    def has_module_perms(self,app_label):
        return True