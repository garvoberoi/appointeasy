from django.contrib import admin
from home.models import Appoint,Contact,Doctor
# Register your models here.

class AdminDoctor(admin.ModelAdmin):
    list_display = ['docid', 'name', 'add', 'category', 'price']

admin.site.register(Appoint)
admin.site.register(Contact)
admin.site.register(Doctor, AdminDoctor)

