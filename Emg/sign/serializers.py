from djoser import serializers
from django.contrib.auth import get_user_model  #returns the currently active user model

User = get_user_model()

class UserCreateSerializer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'full_name', 'email')