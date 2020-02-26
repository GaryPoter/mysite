from django.shortcuts import HttpResponseRedirect

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path != '/user_about/login/' and request.path != '/user_about/do_login/':
            if request.session.get('user', None):
                pass
            else:
                return HttpResponseRedirect('/user_about/login')