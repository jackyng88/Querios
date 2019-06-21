from rest_framework import serializers

from users.models import CustomUser


class UserDisplaySerializer(serializers.ModelSerializer):
    # Class for displaying the currently authenticated user

    class Meta:
        model = CustomUser
        fields = ['username']