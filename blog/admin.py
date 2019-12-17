from django.contrib import admin
from .models import *

# Register your models here.
# class PostInline(admin.TabularInline):
#     model = Post

class PostInline(admin.StackedInline):
    model = Post

class PostAdmin(admin.ModelAdmin):
    list_filter = ['autor', 'data_cadastro', 'titulo']

class AutorAdmin(admin.ModelAdmin):
    inlines = (PostInline, )

admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AutorAdmin)
