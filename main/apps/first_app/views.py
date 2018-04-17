from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def init(request): # goes to the random_word path, goes back to url
    request.session['counter'] = 0
    return redirect('/random_word')

def index(request): #comes here then goes to index
    context = {
        "random" : get_random_string(length=14)
    }
    request.session['counter'] += 1
    return render(request, 'first_app/index.html', context)