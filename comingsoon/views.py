from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from comingsoon.forms import EmailForm


def index(request):
    form = EmailForm()
    return render_to_response('page_coming_soon.html',
        {'form': form},
        context_instance=RequestContext(request))

