from django.contrib.auth import get_user_model 
from rest_framework import serializers 


class RegisterUserSerializer(serializers.ModelSerializer):
    """ Serializer for creating a new user account"""

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'fullname', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 6},
                        'username': {'min_length': 3}}

    def create(self, validated_data):
        """Create a new user with enctrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class UserInfoSerializer(serializers.ModelSerializer):
    """Serializers for the user settings objects"""

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username', 'password', 'fullname', 
                    'bio', 'profile_pic']
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 6},
                        'username': {'min_length': 3}}

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user 


