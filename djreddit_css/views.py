from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

import models

def index(request):
    return render_to_response('djreddit_css/index.html',
        locals(),
        context_instance=RequestContext(request)
    )
    
def add_user(request):
    return render_to_response('djreddit_css/add_user.html',
        locals(),
        context_instance=RequestContext(request)
    )

def list_css(request):
    return render_to_response('djreddit_css/list_css.html',
        locals(),
        context_instance=RequestContext(request)
    )
    
def display_css(request, css_id):
    return render_to_response('djreddit_css/subreddit.css',
        locals(),
        context_instance=RequestContext(request)
    )