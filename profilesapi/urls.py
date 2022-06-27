from email.mime import base
from django.db import router
from django.urls import path, include
from profilesapi import views
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    # path('hello-view/', views.HelloApiView.as_view()),
    # path('', include(router.urls))
    path('', include(router.urls))
]
