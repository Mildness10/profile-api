from encodings import search_function
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from profilesapi import serializers, models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profilesapi import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    
class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated,)
    
    
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
    