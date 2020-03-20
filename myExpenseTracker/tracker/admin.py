from django.contrib import admin
from .models import  categories, expense, budget

# Register your models here.

admin.site.register(categories)
admin.site.register(expense)
admin.site.register(budget)