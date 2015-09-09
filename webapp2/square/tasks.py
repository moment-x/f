from celery import shared_task

from others.qcloud.push import qpush

@shared_task
def send_square_push(square_id, sender_contact, receiver_token):
    alert = '{}发你文件'.format(sender_contact)
    custom = {
        'type': 'file',
        'sender': sender_contact,
        'square_id': square_id
    }
    cstdict = {'custom': custom}
    msg = qpush.build_ios_msg(alert, cstdict)
    qpush.push_token(msg, receiver_token)