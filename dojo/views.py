from django.shortcuts import render
from django.http import HttpResponse

# request: HttpRequest
def mysum(request, x, y):
    return HttpResponse(int(x)+int(y))

def hello(request, name, age):
    return HttpResponse("안녕하세요. {}. {} 살이시네요 ".format(name, age))