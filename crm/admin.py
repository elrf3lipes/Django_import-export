from django.contrib import admin

# Register your models here.

from .models import Parser
from import_export.admin import ImportExportModelAdmin

@admin.register(Parser)
class ParserAdmin(ImportExportModelAdmin):
    list_display = ('Full_Affilation', 'Simplified_Affiliation_for_collapsing', 'store_in_database')
    # Add any other customization you need for the admin view