from django.contrib import admin
from .models import Doctor,department

# Register your models here.

class doctadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','img','qualification','slug','depart']
    list_editable = ['qualification']
admin.site.register(Doctor,doctadmin)

class departadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(department,departadmin)
