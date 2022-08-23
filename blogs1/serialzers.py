from pyexpat import model
from random import choices
from urllib import response
from rest_framework import serializers
from .models import Blog, BlogComment, BlogReaction
from jobs.serializers import JobsGetSerializer

'''serializer for posting blog'''
class BlogPostSerializers(serializers.ModelSerializer):

    class Meta:

        model = Blog
        fields = ['title', 'content']

'''serialier for getting blog'''
class BlogsGetSerializers(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    

    class Meta:

        model = Blog

        fields = ['title', 'profile']

    def get_profile(self, obj):
        
        DP = str(obj.profile.profile_photo)
        response = {
            'Last Name': obj.profile.last_name,
            'DP': DP

        }
        return response
    

        


'''serializer for getting comment of blog'''
class CommentGetSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    class Meta:
        model = BlogComment
        fields = ['user','comment','updated_at'] 
    def get_user(self,obj):
        response = obj.user.email
        return response 

'''serializr for getiing full blog details'''
class BlogsGetDetailsSerializers(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    comments = CommentGetSerializer(source ='blog_comment',many = True ,read_only = True)
    

    class Meta:

        model = Blog

        fields = [ 'profile','title', 'content', 'like','comments']

    def get_profile(self, obj):

        DP = str(obj.profile.profile_photo)
        response = {
            'Last Name': obj.profile.last_name,
            'DP': DP

        }
        return response

'''serializer for posting a comment on blog'''


class CommentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogComment

        fields = ['id','comment','blog']

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:

        model = BlogReaction
        fields = ['id','type','blog'] 



class Likecounter():

    def count(self,validated_data):


        try:

            id = validated_data.get('blog')
            like_num = BlogReaction.objects.filter(blog=id,type='L').count()
        except:
            
            id = validated_data.blog.id  
            
            like_num = BlogReaction.objects.filter(blog=id,type='L').count()  
        
        instance = Blog.objects.get(id=id)
        instance.like = like_num
        instance.save()


        

        

        

    
