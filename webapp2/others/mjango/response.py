from django.http import JsonResponse

def costa(code=None, msg=None, data=None):
    res = {'code': code, 'msg': msg, 'data': data}
    return JsonResponse(res)

class CostaResponse(JsonResponse):
    def __init__(self, code=None, msg=None, data=None):
        res = {'code': code, 'msg': msg, 'data': data}
        super(CostaResponse, self).__init__(res, safe=False)