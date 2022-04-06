from django.contrib import admin
from .models import CovidData
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CovidResource(resources.ModelResource):
    class Meta:
        model = CovidData

class CovidAdmin(ImportExportModelAdmin):
    resource_class = CovidResource

admin.site.register(CovidData, CovidAdmin)
