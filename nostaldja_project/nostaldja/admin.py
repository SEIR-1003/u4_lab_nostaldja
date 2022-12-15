from django.contrib import admin

# Register your models here.
from .models import Fads, Decade

admin.site.register(Fads)
admin.site.register(Decade)