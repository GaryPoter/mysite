from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

# Create your views here.


def login(request):
    title = '登陆页面'
    context = locals()
    return render(request, 'user_about/login.html', context)

def do_login(request):
    if request.POST:
        content = request.POST
        name = content['user']
        password = content['paswd']
        if password == 'admin':
            request.session['user'] = name
        return HttpResponseRedirect('/devices_collect/')