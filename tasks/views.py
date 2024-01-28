from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Create your views here.
def tasks(request):
    template = loader.get_template('myfirst.html')
    tasks = Todo.objects.all().values()
    return HttpResponse(template.render({'tasks': tasks}, request))