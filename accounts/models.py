from django.db import models

from django.contrib.auth.models import AbstractUser

import random

import uuid

from django.utils import timezone

class user(AbstractUser):
    username=None
    email=models.EmailField(max_length=100,unique=True)
    
    USERNAME_FIELD='email'
    
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.email
    
    
class OTP(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)
    create_at=models.DateTimeField(auto_now_add=True)
    uid=models.UUIDField(editable=False,default=uuid.uuid4,primary_key=True)
    
    def save(self,*args,**kwargs):
        self.otp='{:06d}'.format(random.randint(0,999999))
        super().save(*args, **kwargs)
    
        
    def is_expired(self):
        return (timezone.now() - self.create_at).total_seconds() > 120    
        
    