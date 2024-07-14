from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers.loginserilizer import LoginSerilaizer

class LoginView(APIView):
    
    def post(self,request):
        
        serilizer=LoginSerilaizer(data=request.data)
        
        if serilizer.is_valid():
            return Response(serilizer.validated_data)
        
        return Response(serilizer.errors)
        