from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return HttpResponse("TODO-index page")

def list_all(request):
  return