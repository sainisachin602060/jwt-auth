
from rest_framework import serializers
from accounts.models import user
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

class LoginSerilaizer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    
    def validate(self,data):
        email=self.initial_data.get('email')
        password=self.initial_data.get('password')
        
       
        
        try:
            current_user=user.objects.filter(email=email).exists()
        
        except Exception as e:
            raise serializers.ValidationError("email address does not exit")  
        
        user1= authenticate(email=email,password=password) 
        
        
        if user1 is not None:
            
            refesh=RefreshToken.for_user(user1)
            
            return {
                
                'access_token':str(refesh.access_token),
                
                'refresh_token':str(refesh),
            }
            
        else:
            raise serializers.ValidationError("inavalid email and password")
        