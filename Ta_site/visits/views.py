from django.shortcuts import render
from django.views import generic

from .models import Visit


class IndexView(generic.ListView):
    template_name = "visits/index.html"
    context_object_name = "visit_list"

    def get_queryset(self):
        return Visit.objects.all()


def article(request, pk):
    """Shows the article for the specified visit"""
    return render(request, "visits/article.html", context={"article_name": "visits/articles/visit_{}.html".format(pk)})
