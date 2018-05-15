from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Glacier

# Create your views here.


class IndexView(generic.ListView):
    template_name = "glaciers/index.html"
    context_object_name = "glacier_list"

    def get_queryset(self):
        """Return five first glaciers"""
        return Glacier.objects.all()[:5]