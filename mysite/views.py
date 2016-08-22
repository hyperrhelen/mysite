from django.http import HttpResponse
from django.shortcuts import render_to_response
# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
# from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def login(request):
    c = {}
    # c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  user = auth.authenticate(username=username, password=password)

  if user is not None:
    auth.login(request, user)
    return HttpResponseRedirect('/accounts/loggedin')
  else:
    return HttpResponseRedirect('/accounts/invalid')

def logout(request):
  auth.logout(request)
  return render(request, 'logout.html')

def loggedin(request):
  return render(request,'loggedin.html', {'full_name': request.user.username})
  return

def invalid_login(request):
  return render(request, 'invalid_login.html')

def register_user(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/accounts/register_success')
  args = {}
  # args.update(csrf(request))
  args['form'] = UserCreationForm()
  prints(args)
  return render(request, 'register.html', args) 

def register_success(request):
  return render(request, 'register_success.html')
