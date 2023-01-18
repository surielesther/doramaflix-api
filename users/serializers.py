from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            'id',
            'username',
            'email',
            'password',
            'created_at',
            'is_admin',
            'is_superuser',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance