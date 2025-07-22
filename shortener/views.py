from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import ShortURL
from .serializers import ShortURLSerializer

class CreateShortURL(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RedirectShortURL(APIView):
    def get(self, _, code):
        url = get_object_or_404(ShortURL, short_code=code)
        return redirect(url.original_url)