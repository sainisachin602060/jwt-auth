

from accounts.serializers.otprequest_Serilizer import OtpRequestSerilizer
from rest_framework.views import APIView
from accounts.models import OTP
from rest_framework.response import Response

class OtpRequest(APIView):
    
    def post(self,request):
        
        serilizer=OtpRequestSerilizer(data=request.data)
        
        if serilizer.is_valid():
            uuid=serilizer.save()
            return Response({'uuid':str(uuid)})
        return Response(serilizer.errors)


    def get(self,request):
        data=OTP.objects.all()
        
        serdata=OtpRequestSerilizer(data,many=True)
        return Response(serdata.data)
        
    
