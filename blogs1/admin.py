from django.contrib import admin

from .models import Blog, BlogComment, BlogReaction

admin.site.register(Blog)
admin.site.register(BlogReaction)
admin.site.register(BlogComment)
