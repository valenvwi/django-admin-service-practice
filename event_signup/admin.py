from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("-first_name",) # descending order, add - before field name
    readonly_fields = ("email", "date_created")

admin.site.register(Form, FormAdmin)
# Register your models here.
