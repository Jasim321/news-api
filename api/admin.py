from django.contrib import admin
from .models import Articles,Author, Category
# Register your models here.

admin.site.register(Articles)
admin.site.register(Author)
admin.site.register(Category)
