from django.contrib import admin

from .models import Massif, Glacier


class GlacierInline(admin.TabularInline):
    model = Glacier
    extra = 1


class MassifAdmin(admin.ModelAdmin):
    fields = ["massif_name"]

    inlines = [GlacierInline]

class GlacierAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,             {"fields": ["massif", "glacier_name"]}),
        ("Properties",     {"fields": ["glacier_length", "glacier_area"]})
                ]
    list_display = ["glacier_name", "massif", "glacier_area"]
    list_filter = ["massif"]
    search_fields = ["glacier_name"]

# Register your models here.
admin.site.register(Massif, MassifAdmin)
admin.site.register(Glacier, GlacierAdmin)