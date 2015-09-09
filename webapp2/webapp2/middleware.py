import json
class DisableCSRFCheck(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

class LoadJsonBody:
    def process_request(self, request):
        request.data = json.loads(request.body.decode())