from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profilesapi import serializers

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        an_apiview = [
            "Possesses the http methods (get, post, patch, put, delete)",
            "Is similar to Django View",
            "Gives you most control over application logic",
            "Is mapped manually to URLS",
        ]
        
        return Response({'message': 'hello', "an_apiview": an_apiview})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Welcome {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk=None):
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})