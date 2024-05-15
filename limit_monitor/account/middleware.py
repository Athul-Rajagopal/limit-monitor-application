from django.conf import settings
from django.shortcuts import redirect

class PreventLoginRegisterRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            if request.path == settings.LOGIN_URL or request.path == settings.REGISTER_URL:
                return redirect('list_limits')  # Redirect to home page or any other authenticated page

        return response
