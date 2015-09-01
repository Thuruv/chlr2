from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render, Http404
from django.core.urlresolvers import reverse, Http404
from django.template import Context

from .models import Post
from .forms import PostModelForm

def gindex(request):
    two_days_ago = datetime.utcnow() - timedelta(days=2)
    recent_posts = Post.objects.filter(created_at__gt=two_days_ago).all()
    context = Context({
        'post_list': recent_posts
    })
    return render(request, 'index.html', context)


# post_detail accepts two arguments: the normal request object and an integer
# whose value is mapped by post_id defined in r'^post/(?P<post_id>\d+)/detail.html$'
def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        # If no Post has id post_id, we raise an HTTP 404 error.
        raise Http404
    return render(request, 'post/detail.html', {'post': post})

def post_upload(request):
    form  = PostModelForm(request.POST or None)
    if form.is_valid():
        f = form.save(commit = False)
        f.save()
        return HttpResponseRedirect('')
    else:
        form = PostModelForm()
    context = {
    "form" : form
    }
    template = 'upload.html'
    return render(request,template,context)


def all_view(request):
    all = Post.objects.all()
    return render(request, 'post/all.html', {'all_view': all})
