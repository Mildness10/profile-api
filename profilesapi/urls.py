from django.urls import path
from profilesapi import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
