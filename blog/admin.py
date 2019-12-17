from django.contrib import admin
from .models import *

# Register your models here.
class PostInline(admin.TabularInline):
    model = Post

class AutorAdmin(admin.ModelAdmin):
    inlines = (PostInline, )

admin.site.register(Post)
admin.site.register(Autor, AutorAdmin)
