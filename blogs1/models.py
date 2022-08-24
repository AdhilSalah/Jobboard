from django.db import models

# Create your models here.
from ast import mod
from turtle import title, update
from django.db import models
from mainuser.models import NewUser, Userprofile
from django.utils.translation import ngettext_lazy
from django.utils.deconstruct import deconstructible
from django.core.validators import BaseValidator


@deconstructible
class MinLengthValidator(BaseValidator):
    message = ngettext_lazy(
        "Ensure this value has at least %(limit_value)d character (it has "
        "%(show_value)d).",
        "Ensure this value has at least %(limit_value)d characters (it has "
        "%(show_value)d).",
        "limit_value",
    )
    code = "min_length"

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)

class Blog(models.Model):

    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    profile = models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    content = models.TextField()
    like = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title


class BlogReaction(models.Model):

    FEEDBACK_OPTIONS = (
        ('L', 'Like'),
        ('D', 'Dislike'),
    )
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=1,choices=FEEDBACK_OPTIONS)

    def __str__(self):

        return self.blog.title

class BlogComment(models.Model):

    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    comment = models.TextField(validators=[MinLengthValidator(3)]) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):

        return self.blog.title


class CommentReply(models.Model):

    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    comment = models.ForeignKey(BlogComment,on_delete=models.CASCADE,related_name='reply_to_comment')
    reply = models.TextField(validators=[MinLengthValidator(3)]) 
    updated_at = models.DateTimeField(auto_now=True)        
    
