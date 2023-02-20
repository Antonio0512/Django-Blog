from django.contrib import admin
from blog.web_blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass