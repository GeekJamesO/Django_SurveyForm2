from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import bcrypt
def index(request):
    context = { }
    return render(request, "surveys_app/index.html", context)

def process(request, methods=['POST']):
    context = { }
    try:
        request.session['counter'] += 1
    except Exception as e:
        request.session['counter'] = 1

    try:
        yourName = request.POST['yourName']
        dojoLocation = request.POST['dojoLocation']
        favLanguage = request.POST['favLanguage']
        comment = request.POST['comment']
    except Exception as e:
        messages.append("Exception thrown:", str(e))
        return redirect('/')
    if len(yourName) == 0:
        messages.debug(request, 'Your Name can not be blank.')
    if len(dojoLocation) == 0:
        messages.debug(request, 'Dojo Location can not be blank.')
    if len(favLanguage) == 0:
        messages.debug(request, 'Fav Language can not be blank.')
    if len(comment) == 0:
        messages.debug(request, 'Comment can not be blank.')
    if len(comment) > 640:
        messages.debug(request, 'Comment can not be more thanb 640 characters.')

    request.session['yourName'] = yourName
    request.session['dojoLocation'] = dojoLocation
    request.session['favLanguage'] = favLanguage
    request.session['comment'] = comment
    return redirect('/results')

def results(request):
    return render(request, "surveys_app/results.html")
