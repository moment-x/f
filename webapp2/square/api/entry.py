from square.models import Square, Extra, DeliverySquare, EverNoteAuthTrack
from square.serializers import SquareSerializer, DeliverySquareSerializer
from user.models import User
from square.tasks import send_square_push
from django.http import (HttpResponse, JsonResponse)
from others.qcloud.image.qimage import multi_entry_sign

from square.api.migrate import get_access_token, get_all_note_guid, get_note_content, parse_html
from evernote.api.client import EvernoteClient
from others.qcloud.image.qimage import upload

import json

def download(request):
    serializer = SquareSerializer(request.user.square_set.filter(active=True), many=True)
    return JsonResponse(serializer.data)


def upload(request):
    data = json.loads(request.body.decode())
    if hasattr(data,'extra'):
        data['extra'] = Extra.objects.create(**data['extra'])
    square = Square.objects.create(owner=request.user, **data)
    serializer = SquareSerializer(square)
    return JsonResponse(serializer.data)


def send(request):
    data = json.loads(request.body.decode())
    sender = request.user
    receiver = sender.friend.filter(contact=data['receiver'])
    square_id = data['square_id']
    if receiver.exists():
        DeliverySquare(square_id=square_id, receiver=receiver).save()
        if hasattr(receiver, 'token'):
            send_square_push.delay(square_id, sender.contact, receiver.token)
    return HttpResponse('done')


def receive(request):
    data = json.loads(request.body.decode())
    square_id = data['square_id']
    receiver = request.user
    query = DeliverySquare.objects.filter(square_id=square_id, receiver=receiver)
    if query.exists():
        square = Square.objects.get(id=square_id)
        serializer = SquareSerializer(square)
        return JsonResponse(serializer.data)


def in_delivery(request):
    user = request.user
    squares = DeliverySquare.objects.filter(receiver=user)
    serializer = DeliverySquareSerializer(squares, many=True)
    return JsonResponse(serializer.data, safe=False)


def qsign(request):
    sign = multi_entry_sign('avatar')
    return JsonResponse(sign, safe=False)


def migrate_all_notes(request):
    access_token = get_access_token(request.user)
    guid_list = get_all_note_guid(access_token)
    for note_guid in guid_list:
        title, html, image_byte = get_note_content(note_guid, access_token)
        paragraph = parse_html(html)
        image_url = upload(image_byte, 'avatar')
        Square.objects.create(owner=request.user, title=title, paragraph=paragraph, image=image_url)


def evernote_auth(request):
    from square.api.migrate import evernote_auth_url
    return JsonResponse({'url': evernote_auth_url(request.user)})


def evernote_auth_callback(request):
    oauth_verifier = request.GET['oauth_verifier']
    oauth_token = request.GET['oauth_token']
    track = EverNoteAuthTrack.objects.get(oauth_token=oauth_token)
    track.oauth_verifier = oauth_verifier
    track.save()
    return JsonResponse({'url': '1'})