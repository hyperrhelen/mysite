from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import loader
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# def login_view(request):
#   m = User.objects.get(username=request.POST['username'])
#   if m.password == request.POST['password']:
#     request.session['member_id'] = m.id
#     return HttpResponse("You're logged in.")
#   else:
#     return HttpResponse("Your username and password did not match")

# def logout(request):
#   try: 
#     del request.session['member_id']
#   except KeyError:
#     pass
#   return HttpResponse("You're logged out.")