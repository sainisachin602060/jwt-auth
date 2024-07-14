

from rest_framework import serializers
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER

from accounts.models import OTP,user
class ResendOtpser(serializers.Serializer):
    
    email=serializers.CharField()
   
   
    def validate_email(self,email):
        try:
           cuser=user.objects.get(email=email)
        except Exception as e:
            raise serializers.ValidationError("email not exit")
        return email
    
     
   
   
    def send_otp_email(self,email,otp):
        
        send_mail(
            subject="Password otp",
            message=f"your otp is {otp}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
            
        )

        
        
    def save(self):
        cuser=user.objects.get(email=self.validated_data['email'])
        exiting_otp=OTP.objects.filter(user=cuser).first()
        
        if exiting_otp and not exiting_otp.is_expired():
            raise serializers.ValidationError("otp sent aready")
        else:
            new_otp=OTP.objects.create(user=cuser)
            new_otp.save()
            
            self.send_otp_email(cuser.email,new_otp.otp)
            
            return new_otp.otp
        
        
    
         
    
    
    