from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def index(request):
    return render_to_response('page_coming_soon.html',
        context_instance=RequestContext(request))

