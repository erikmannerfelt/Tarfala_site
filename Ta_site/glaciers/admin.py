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
        ("Properties",     {"fields": ["glacier_length"]})
                ]

# Register your models here.
admin.site.register(Massif, MassifAdmin)
admin.site.register(Glacier, GlacierAdmin)