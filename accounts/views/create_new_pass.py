from rest_framework.views import APIView
from rest_framework import serializers
from accounts.serializers.create_ner_Ser import CreateNewPass
from rest_framework.response import Response




class Create_New_Pass(APIView):
    
    def post(self,request):
        serilizer=CreateNewPass(data=request.data)
        
        if serilizer.is_valid():
            serilizer.save()
            return Response(data="new pass cretaed")
        
        return Response(data=serilizer.errors)
    