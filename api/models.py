from django.db import models
from conf import settings
from .decorators import UploadTo
# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=30)
    university_cart = models.CharField(max_length=50)

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'



class Student(models.Model):
    DOCUMENTS = (
        "passport",        
        "photo",
        "university_cert",    
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    passport_number = models.CharField(
        max_length=255, unique=True
    )
    
    address = models.CharField(max_length=255)
    agree_with_agreement = models.BooleanField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    passport = models.FileField(
        upload_to=UploadTo('passport')
    )
    university_cert = models.FileField(
        null=True, blank=True, upload_to="uploads/%Y/%m/%d"
    )
    photo = models.FileField(
        null=True, blank=True, upload_to="uploads/%Y/%m/%d"
    )

    price = models.DecimalField(max_digits=8,decimal_places=2,default=0)



class Sponsor(models.Model):    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    passport_number = models.CharField(
        max_length=255, null=True, unique=True, blank=True
    )

    address = models.CharField(max_length=255, null=True)
    agree_with_agreement = models.BooleanField(default=False)

    passport = models.FileField(
        upload_to=UploadTo('passport')
        
        
    )
    photo = models.FileField(
        null=True, blank=True, upload_to="uploads/%Y/%m/%d"
    )

    price = models.DecimalField(max_digits=8,decimal_places=2,default=0)