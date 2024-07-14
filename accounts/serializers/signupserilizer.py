

from rest_framework.serializers import ModelSerializer
from accounts.models import user
from rest_framework import serializers

class Signupserilizer(ModelSerializer):
    first_name=serializers.CharField(allow_blank=True,required=False)
    last_name=serializers.CharField(allow_blank=True,required=False)
    
    
    class Meta:
        model=user
        fields=['first_name','last_name','email','password']
        extra_kwargs={'password':{'write_only':True}}
        
    def create(self, validated_data):
        
        new_user=user.objects.create(first_name=validated_data['first_name'],
                            last_name=validated_data['last_name'],
                            email=validated_data['email'],
                           )   
        new_user.set_password(validated_data['password'])
        new_user.save()
        
        return new_user