from django.urls import path
from .views import UserProfileView

urlpatterns = [
    path('<slug:my_slug>/', UserProfileView.as_view())
]
