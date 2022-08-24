from django.contrib import admin

from .models import Blog, BlogComment, BlogReaction, CommentReply

admin.site.register(Blog)
admin.site.register(BlogReaction)
admin.site.register(BlogComment)
admin.site.register(CommentReply)
