from django.contrib import admin
from .models import ProfileFeedItem, UserProfile

#REGISTERING OF MODELS IN ADMIN SITE
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
