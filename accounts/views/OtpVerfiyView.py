
from rest_framework.views import APIView
from rest_framework import serializers
from accounts.serializers.otpverfiyserilizer import Otp_Verify_Serilizer
from rest_framework.response import Response


class OtpVerfiyView(APIView):
    
    def post(self,request):
        serilizer=Otp_Verify_Serilizer(data=request.data)
        
        if serilizer.is_valid():
            uuid=serilizer.save()
            
            return Response(uuid)
        
        return Response(serilizer.errors)
    