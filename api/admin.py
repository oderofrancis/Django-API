from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle','author','isbn')

admin.site.register(Book,BookAdmin)