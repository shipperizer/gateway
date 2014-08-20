from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from repos.models import Repo, File
import logging

logger = logging.getLogger()


class IndexView(generic.ListView):
    template_name = 'repos/index.html'
    context_object_name = 'repo_list'

    def get_queryset(self):
        return Repo.objects.all()

class DetailView(generic.DetailView):
    model = Repo
    template_name = 'repos/detail.html'

class FilesView(generic.ListView):
    template_name = 'repos/files.html'
    context_object_name = 'file_list'
    
    def get_queryset(self):
        return Repo.objects.get(self.object.id).file_set.all()

def delete(request, file_id):
    file = File.objects.get(pk=file_id)
    return HttpResponseRedirect("DELETE %s." % file.url )