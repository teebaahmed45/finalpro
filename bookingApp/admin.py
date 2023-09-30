from django.contrib import admin
from .models import categories,courses,booking
# Register your models here.

admin.site.register(booking)
admin.site.register(courses)
admin.site.register(categories)


