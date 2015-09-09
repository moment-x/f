from celery import shared_task

from others.qcloud.push import qpush

@shared_task
def add_friend_push(sender_contact, receiver_token):
    alert = '{}加你好友'.format(sender_contact)
    custom = {
        'type': 'friend',
        'sender': sender_contact,
    }
    cstdict = {'custom': custom}
    msg = qpush.build_ios_msg(alert, cstdict)
    qpush.push_token(msg, receiver_token)
