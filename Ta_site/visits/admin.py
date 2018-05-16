from django.contrib import admin

from .models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ["name", "visit_title", "visitor_name", "visit_year"]

    # Mostly to remember syntax
    def name(self, obj):
        return obj.citation

admin.site.register(Visit, VisitAdmin)
