from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

import models, forms

def index(request):
    subreddits = models.SubReddit.objects.all()
    return render_to_response('djreddit_css/index.html',
        locals(),
        context_instance=RequestContext(request)
    )
    
def add_user(request):
    instance = None
    if request.GET.get('grouping_id'):
        grouping = get_object_or_404(models.Grouping, 
            id=request.GET.get('grouping_id')
        )
        instance = models.RedditUser(grouping=grouping)
    form = forms.RedditUserForm(instance=instance)
    if request.method == 'POST':
        form = forms.RedditUserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    return render_to_response('djreddit_css/add_user.html',
        locals(),
        context_instance=RequestContext(request)
    )

def list_css(request):
    subreddits = models.SubReddit.objects.all()
    return render_to_response('djreddit_css/list_css.html',
        locals(),
        context_instance=RequestContext(request)
    )
    
def display_css(request, css_id):
    subreddit = get_object_or_404(models.SubReddit, id=css_id)
    return render_to_response('djreddit_css/subreddit.css',
        locals(),
        context_instance=RequestContext(request)
    )