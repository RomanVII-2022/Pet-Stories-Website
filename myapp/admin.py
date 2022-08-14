from django.contrib import admin
from .models import Category, Story, Contact

# Register your models here.
admin.site.register(Story)
admin.site.register(Category)
admin.site.register(Contact)

