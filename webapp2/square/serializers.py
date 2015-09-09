from rest_framework import serializers

from square.models import Square, DeliverySquare


class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Square
        fields = ('extra', 'title', 'paragraph', 'image')
        depth = 1

class DeliverySquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverySquare
        fields = ('square',)