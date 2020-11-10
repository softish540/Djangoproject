from django.shortcuts import render
from django.http import HttpResponse

# this file renders a code to a view
def index(request):# pass in request parameter to be responded
    return HttpResponse("<h1>Hello World!!</h1>")# response 


