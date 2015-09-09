from user.serializers import UserSerializer, TokenSerializer
from user.models import User


def user_info_feed(user):
    serializer = UserSerializer(user)
    return {'user_info_feed': serializer.data}


def user_friend_info_feed(user):
    serializer = UserSerializer(user.friend, many=True)
    return {'user_friend_info_feed': serializer.data}


def user_friend_request_feed(user):
    add_list = User.objects.filter(friend_request=user)
    serializer = UserSerializer(add_list, many=True)
    return {'user_friend_request_feed': serializer.data}