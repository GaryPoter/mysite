from django.shortcuts import render

# Create your views here.


def login(request):
    title = '登陆页面'
    context = locals()
    return render(request, 'user_about/login.html', context)