from rest_framework import serializers

from user.models import User, Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('token',)

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
         return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ('contact', 'gender', 'avatar', 'date_of_birth', 'nickname')
        depth = 1