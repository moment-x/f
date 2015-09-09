import tencentyun

import time
import uuid

from others.qcloud.image.config import (SECRET_ID, SECRET_KEY, APPID, BUCKET)


AUTH = tencentyun.Auth(SECRET_ID, SECRET_KEY)
MANAGER = tencentyun.ImageV2(APPID, SECRET_ID, SECRET_KEY)

def multi_entry_sign(which, fileid=''):
    expired = int(time.time()) + 999
    sign = AUTH.get_app_sign_v2(BUCKET[which], fileid, expired)
    return sign


def upload(image, which):
    bucket = BUCKET[which]
    fileid = str(uuid.uuid4())
    obj = MANAGER.upload_binary(image, bucket, fileid)
    if obj['code'] == 0:
        return obj['data']['download_url']
