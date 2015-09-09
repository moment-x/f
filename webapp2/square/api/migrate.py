from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec

from others.mjango.field import filter_kwargs
from square.models import EverNoteAuthTrack

client = EvernoteClient(
    consumer_key='rivennote',
    consumer_secret='31c04102552a86a2',
    sandbox=True
)

def evernote_auth_url(user):
    request_token = client.get_request_token('115.159.87.59/square/evernote_auth_callback')
    auth_track_args = filter_kwargs(EverNoteAuthTrack, request_token)

    EverNoteAuthTrack.objects.create(owner=user, **auth_track_args)
    url = client.get_authorize_url(request_token)
    return url


def get_access_token(user):
    try:
        recent_track = user.evernoteauthtrack_set.order_by('-id')[0:1].get()
    except EverNoteAuthTrack.DoesNotExist:
        raise
    if recent_track.oauth_verifier is None:
        return
    access_token = client.get_access_token(
        recent_track.oauth_token,
        recent_track.oauth_token_secret,
        recent_track.oauth_verifier
    )
    return access_token


def get_all_note_guid(access_token):
    client = EvernoteClient(token=access_token)
    note_store = client.get_note_store()
    board_filter = NoteFilter()
    result_spec = NotesMetadataResultSpec()
    result_list = note_store.findNotesMetadata(
        access_token, board_filter, 0, 100, result_spec)
    # High-level info of notes obtained  in result_list
    note_guid_list = [note.guid for note in result_list.notes]
    return note_guid_list


def find_first_image(resources):
    if resources:
        for resource in resources:
            if resource.mime.startswith('image'):
                return resource


def get_note_content(guid, access_token):
    client = EvernoteClient(token=access_token)
    note_store = client.get_note_store()
    note = note_store.getNote(access_token, guid, False, False, False, False)
    title = note.title
    html = note.content
    resources = note.resources
    first_image = find_first_image(resources)
    first_image_data = note_store.getResourceData(access_token,first_image.guid)
    return title, html, first_image_data


def migrate_all_notes(request):
    access_token = get_access_token(request.user)
    client = EvernoteClient(token=auth_token)
    userStore = client.get_user_store()
    user = userStore.getUser()


def parse_html(html):
    from bs4 import BeautifulSoup
    bsObj = BeautifulSoup(html)
    return bsObj.html.get_text()