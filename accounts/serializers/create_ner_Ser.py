
from rest_framework import serializers
from accounts.models import user,OTP



class CreateNewPass(serializers.Serializer):
    uuid=serializers.CharField()
    new_password=serializers.CharField(write_only=True)
    
    
    def validate(self, attrs):
        uuid=attrs.get('uuid')
        
        
        try:
            
            otpuser=OTP.objects.get(uid=uuid)
        except OTP.DoesNotExist:
            raise serializers.ValidationError("uuid not match")    
        
        return attrs
    
    def save(self, **kwargs):
        
        uuid=self.validated_data['uuid']
        
        new_password=self.validated_data['new_password']
        
        
        otp_user=OTP.objects.get(uid=uuid)
        
        curent_user=otp_user.user
        
        curent_user.set_password(new_password)
        
        curent_user.save()
        
        otp_user.delete()
        
        return curent_user
        
        
            
            
            
            
        
        