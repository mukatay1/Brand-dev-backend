from django.contrib import admin
from .models import UserAccount, UserProfile

# Register your models here.
@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name', 
        'email', 
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'phone',
        'slug'
    )