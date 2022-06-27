from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profilesapi import serializers, models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profilesapi import permissions


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)