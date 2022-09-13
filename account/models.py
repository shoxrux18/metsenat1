from contextlib import nullcontext
from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given username and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number, password)
        user.is_staff = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    class Roles(models.TextChoices):
        STUDENT = "student"
        SPONSOR = "sponsor"
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=Roles.choices)
    phone_number = PhoneNumberField(unique=True)
    objects = CustomUserManager()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{str(self.phone_number)}"
