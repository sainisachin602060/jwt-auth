

from rest_framework import serializers

from accounts.models import OTP

class Otp_Verify_Serilizer(serializers.Serializer):
    
    uuid=serializers.CharField()
    otp=serializers.CharField(max_length=6)
    
    
    
    def validate_otp(self,otp):
        
        if len(otp)<6 and len(otp)>6:
            raise serializers.ValidationError("otp is invalid")
        return otp

        
        
    def validate(self,data):
        uuid=data.get('uuid') 
        otp=data.get('otp') 
        
        
        
            
            
        try:
            otp_instance=OTP.objects.get(uid=uuid,otp=otp) 

        except OTP.DoesNotExist:
            
            raise serializers.ValidationError("invalid otp")    
        
        if otp_instance.is_expired():
            raise serializers.ValidationError("otp has expried")
        
        return {'uuid':uuid}
    
    
    def create(self, validated_data):
        return validated_data
        
          
    
    
