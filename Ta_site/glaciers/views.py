from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Glacier, Massif
from django.shortcuts import get_object_or_404

# Create your views here.


class IndexView(generic.ListView):
    """Displays every available glacier"""
    template_name = "glaciers/index.html"
    context_object_name = "glacier_list"

    def get_queryset(self):
        """Return every glacier"""
        return Glacier.objects.all()


def article(request, pk):
    """Shows the article for the specified glacier"""
    return render(request, "glaciers/article.html", context={"article_name": "glaciers/articles/glacier_{}.html".format(pk)})


class MassifView(generic.ListView):
    """Displays every available massif"""
    template_name = "glaciers/massifs.html"
    context_object_name = "massifs_list"

    def get_queryset(self):
        """Return every massif"""
        return Massif.objects.all()

class MassifGlacierView(generic.ListView):
    """Displays every glacier in the chosen massif"""
    template_name = "glaciers/massif_glaciers.html"
    context_object_name = "glacier_list"

    def get_queryset(self):
        """Return every glacier in a certain massif, and gets the massif pk from the url"""
        self.massif = self.kwargs["pk"]
        return Glacier.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MassifGlacierView, self).get_context_data(**kwargs)  # Get previous context

        context["massif_pk"] = self.massif  # Add massif to context

        return context

