
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'../ ../'))
sys.path.append(BASE_DIR)

from ml_model.generate import generate_text

class GenerateText(APIView):
    def post(self,request):
        prompt = request.data.get("prompt")
        output = generate_text(prompt)
        return Response({"generated_text":output})
