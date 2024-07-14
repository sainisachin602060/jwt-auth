from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers.signupserilizer import Signupserilizer
from accounts.models import user

class SignupView(APIView):
    
    def post(self,request):
        
        serializer=Signupserilizer(data=request.data)
        
        print(serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





















    def get(self,request):
        serilser_data=user.objects.all()
        
        jsondata=Signupserilizer(serilser_data,many=True)

        return  Response(jsondata.data)
      
    