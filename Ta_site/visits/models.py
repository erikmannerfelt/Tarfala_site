from django.db import models


class Visit(models.Model):
    visitor_first_name = models.CharField(max_length=200, default="")
    visitor_last_name = models.CharField(max_length=200, default="")
    visit_title = models.CharField(max_length=200, default="")
    visit_year = models.IntegerField()

    @property
    def visitor_name(self):
        return "{} {}".format(self.visitor_first_name, self.visitor_last_name)

    @property
    def citation(self):
        return "{} ({})".format(self.visitor_last_name, self.visit_year)

    def __str__(self):
        return self.citation
