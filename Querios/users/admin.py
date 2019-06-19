from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Custom class that extends Django's UserAdmin class
    
    """
    Note -
    In case you want to add other fields to the CustomUser model we need to 
    specify something like ->
    add_form = a custom form class to create new users and
    form = to update different instances
    """
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)