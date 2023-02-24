from django.contrib import admin
from blog_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
