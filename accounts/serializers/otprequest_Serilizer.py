


from rest_framework import serializers
from accounts.models import user
from accounts.models import OTP
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER

class OtpRequestSerilizer(serializers.Serializer):
    
    email=serializers.EmailField()

    
    
    def validate_email(self, email):
    
        try:
            current_user=user.objects.get(email=email)
           
        except user.DoesNotExist:
            raise serializers.ValidationError("email does not exits") 
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
        current_user=user.objects.get(email=self.validated_data['email'])
        
        otp=OTP.objects.create(user=current_user)
        otp.save()
        data=OTP.objects.all()
        
        print(data,len(data))
        
        self.send_otp_email(current_user.email,otp.otp)
        
        return otp.uid
    
