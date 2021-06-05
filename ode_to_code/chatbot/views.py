from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from speech_recognition import AudioFile

from .serializers import requestSerializer

from .functions import audioToText

class api_callView(views.APIView):

    def get(self, request):
        #audio = AudioFile()
        #data= [{"question_key":"q2", "options": ["<5lakh","5lakh-15lakh","15-lakh-20lakh","20lakh>"], "audio" = }]
        data = [request]
        results = requestSerializer(data, many=True).data
        return Response(results)

    def post(self,request):

        if "question_key" not in request.data or "options" not in request.data or "audio" not in request.data:
            return Response("Insufficient Parameters",status=status.HTTP_400_BAD_REQUEST)
        
        options = request.data["options"]
        audio = request.data["audio"]

        transcript = audioToText.speechToTranscript(audio)

        #Function to process

        result = {
            "transcript" : transcript
        }

        return Response(result,status=status.HTTP_200_OK)


    
        

        


def index(request):
    
    return render(request, 'index.html')

