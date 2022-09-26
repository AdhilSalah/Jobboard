from functools import partial
from urllib import request, response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response

from .serialzers import BlogPostSerializers, BlogsGetDetailsSerializers, BlogsGetSerializers, CommentPostSerializer, LikePostSerializer, Likecounter, ReplyPostSerializer
from .models import Blog, BlogComment, BlogReaction, CommentReply

from mainuser.models import Userprofile
from jobs.serializers import JobsGetSerializer
from django.shortcuts import get_object_or_404
import copy
from mainuser.permissions import IsOwnerOrReadOnly
from slugify import slugify
from rest_framework_simplejwt.authentication import JWTAuthentication



'''operations on a blog'''
class BlogView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogPostSerializers
    queryset = Blog.objects.all()

        
    def perform_create(self, serializer):
        slug = slugify('this blog')
        profile = get_object_or_404(Userprofile,user = self.request.user)
        serializer.save(user = self.request.user,profile = profile,slug = slug)
    def retrieve(self, request, pk=None):
        queryset = Blog.objects.all()
        blog = get_object_or_404(queryset, pk=pk)
        serializer = BlogsGetDetailsSerializers(blog) 
        return Response(serializer.data)  


'''Commenting on  a post'''
class PostCommentView(viewsets.ModelViewSet):

    serializer_class = CommentPostSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication,]

    queryset = BlogComment.objects.all()
    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)

'''Liking on post'''

class PostLikeView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication,]
    serializer_class = LikePostSerializer
    queryset = BlogReaction.objects.all()
    
    
    def perform_create(self, serializer):
        like = copy.deepcopy(serializer.validated_data)
        blog= like.pop('blog')

        
        
        if BlogReaction.objects.filter(blog=blog,user=self.request.user).exists():

            pass
        else:

            print('hi2')

            serializer.save(user = self.request.user)


            x= Likecounter()
            x.count(serializer.data)

    

    def perform_update(self, serializer):

        serializer.save()

        x = Likecounter()
        x.count(serializer.data)

        return Response(serializer.data)   

    def perform_destroy(self, instance):

        x = Likecounter()
        x.count(instance)

        
        return super().perform_destroy(instance)   


class ReplyToCommentView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication,]
    serializer_class =   ReplyPostSerializer
    queryset = CommentReply.objects.all()
    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)



            

    
        
    
        

