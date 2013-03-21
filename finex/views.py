from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def login_user(request):
    success = 0
    state = redirect = username = password = ''
    
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                try:
                    state = "Incorrect credentials"
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    state = "Hey, new user!"
                    user = User.objects.create_user(username, '', password)
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    success = 1
                    redirect = '/'
                    return HttpResponseRedirect(reverse('home'))
        return render_to_response(
                                    'auth.html', {
                                        'state':state,
                                        'username': username,
                                        'success': success,
                                        'redirect':redirect,
                                    },
                                    context_instance=RequestContext(request)
                                )

def logout_user(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.user.is_authenticated():
         return render_to_response(
                                     'home.html',
                                     context_instance=RequestContext(request)
                                 )
    else:
        return redirect('login')
