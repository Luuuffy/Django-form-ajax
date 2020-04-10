from django.shortcuts import render
from.models import User
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def create_user(request):
    print("going through")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create(name=email,
                            password=password
                        )

    return HttpResponse('')
