from email.mime import base
from django.db import router
from django.urls import path, include
from profilesapi import views
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
