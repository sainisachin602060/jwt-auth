from accounts.serializers.ResendOtpser import ResendOtpser
from rest_framework.views import APIView
from accounts.models import OTP
from rest_framework.response import Response


class ResendOtp(APIView):
    
    def post(Self,request):
        
        serilizer=ResendOtpser(data=request.data)
        
        if serilizer.is_valid():
            serilizer.save()
            
            return Response("otp has been sent")
        
        return Response(serilizer.errors)