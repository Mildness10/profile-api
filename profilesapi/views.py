from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            "Possesses the http methods (get, post, patch, put, delete)",
            "Is similar to Django View",
            "Gives you most control over application logic",
            "Is mapped manually to URLS",
        ]
        
        return Response({'message': 'hello', "an_apiview": an_apiview})