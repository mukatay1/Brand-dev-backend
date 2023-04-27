from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import UserProfile
from .serializers import UserProfileSerializer


# Create your views here.
class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        slug = self.kwargs.get('my_slug')
        return UserProfile.objects.get(slug=slug)
