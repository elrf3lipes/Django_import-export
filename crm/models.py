from django.db import models
from import_export import resources, fields

class Parser(models.Model):
    Full_Affilation = models.CharField(max_length=150)
    Simplified_Affiliation_for_collapsing = models.CharField(max_length=225)
    store_in_database = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.store_in_database:
            super(Parser, self).save(*args, **kwargs)

class ParserResource(resources.ModelResource):
    class Meta:
        model = Parser

    custom_field = fields.Field(column_name='Custom Field', attribute='store_in_database')
    # Add more fields and customize their behavior as needed

# Now, you can use the `ParserResource` class in your admin.py file
# to configure the import/export behavior in the Django Admin.
