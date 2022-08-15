from django.contrib import admin
from .models import Blog,BlogComment,BlogReaction

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogReaction)
admin.site.register(BlogComment)
