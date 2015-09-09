from django.http import (HttpResponse, JsonResponse)
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.db.utils import IntegrityError
from user.models import User, Token
from user.serializers import UserSerializer
from user.api.feed import (user_info_feed, user_friend_info_feed, user_friend_request_feed, )
from user import tasks
from square.api.feed import square_of_user_feed
from others.mjango.response import CostaResponse

import json
from functools import reduce


def sign_up(request):
    try:
        User.objects.create(**request.data)
    except IntegrityError:
        return CostaResponse('1', 'contact in use')
    return CostaResponse('0', 'OK')


def sign_in(request):
    user = authenticate(**request.data)
    if user:
        login(request, user)
        Token.objects.update_or_create(
            owner=user,
            defaults={'token': request.data['token']}
        )
        return CostaResponse('0', 'OK')
    return CostaResponse('2', 'wrong password')


def sign_in_with_feed(request):
    user = authenticate(**request.data)
    if user:
        login(request, user)
        Token.objects.update_or_create(
            owner=user,
            defaults={'token': request.data['token']}
        )
        feed_content = (
            user_info_feed(user),
            user_friend_info_feed(user),
            user_friend_request_feed(user),
        )
        reduce(lambda a, b: a.update(b) or a, feed_content)
        return CostaResponse('0', 'OK', feed_content[0])
    return CostaResponse('2', 'wrong password')


def sign_out(request):
    logout(request)
    return CostaResponse('0', 'OK')


def validate(request):
    data = request.data
    candidate = set(data['contact'])
    friends = set(
        request.user.friend.all().values(
            'contact', flat=True
            )
        )
    existed = {
        contact for contact in candidate
        if User.objects.get(contact=contact).exists()
        }
    ret = {
        'not_existed': list(candidate - existed),
        'existed_and_friend': list(existed & friends),
        'existed_not_friend': list(existed - friends),
        }
    return CostaResponse('0', 'OK', ret)


def reset_password_login(request):
    backend = request.session['_auth_user_backend']
    user = request.user
    user.set_password(request.data['password'])
    user.save()
    user.backend = backend
    login(request, user)
    return CostaResponse('0', 'OK')


def update_user_info(request):
    request.data['contact'] = request.user.contact
    # keep contact inviriant, password is automatically safe
    serializer = UserSerializer(request.user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return CostaResponse('0', 'OK')


def add_friend(request):
    try:
        friend = User.objects.get(contact=request.data['friend'])
    except User.DoesNotExist:
        return CostaResponse('3', 'OK')
    request.user.friend_request.add(friend)
    if hasattr(friend, 'token'):
        try:
            tasks.add_friend_push.delay(request.user.contact, friend.token)
        except:
            pass
    return CostaResponse('0', 'OK')


def react_friend(request):
    friend = User.objects.get(contact=request.data['friend'])
    is_valid = friend.friend_request.filter(
                   id=request.user.id
                   ).exists()
    if is_valid:
        if request.data['decision'] == 'yes':
            request.user.friend.add(friend)
        friend.friend_request.remove(request.user)
    return CostaResponse('0', 'OK')

