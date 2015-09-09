from others.qcloud.push.config import (ACCESS_ID, SECRET_KEY)

try:
    from . import xinge
except Exception:
    import xinge


x = xinge.XingeApp(ACCESS_ID, SECRET_KEY)


def build_ios_msg(alert, custom):
    msg = xinge.MessageIOS()
    msg.alert = alert
    msg.badge = 1
    msg.custom = custom
    return msg


def push_token(msg, token):
    x.PushSingleDevice(token, msg, xinge.XingeApp.ENV_DEV)