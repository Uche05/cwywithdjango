from django.http import HttpResponseForbidden

ALLOWED_IPS = ['']

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META.get('REMOTE_ADDR') not in ALLOWED_IPS:
            return HttpResponseForbidden("Access denied.")
        return self.get_response(request)
