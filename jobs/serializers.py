from dataclasses import fields
from pyexpat import model
from unicodedata import category
from rest_framework import serializers

from mainuser.serializers import ProfilleGetSerializer
from .models import Category, JobsPosting

from mainuser.models import Userprofile

class CategorySerializers(serializers.ModelSerializer):


    class Meta:

        model= Category
        fields = '__all__'

class Jobuserprofile(serializers.ModelSerializer):


    class Meta:

        model =   Userprofile
        fields = ['profile_photo','last_name']
        

class JobpsotingSerializer(serializers.ModelSerializer):
    


    class Meta:

        model = JobsPosting
        fields = ['category','job_title','job_description']     

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["category"] = CategorySerializers(instance.category.all(), many=True).data
        return rep

class JobsGetSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    


    class Meta:

        model = JobsPosting
        fields = '__all__'   
    def get_profile(self, obj):

        DP=str(obj.profile.profile_photo)
        response={
            'Last Name':obj.profile.last_name,
            'DP':DP
            
        }
        return response
    def get_category(self,obj):

        category = obj.category.all()
        category_array=[]
        for category in category:

            category_array.append(category.category_name)
        
        return category_array
        

    
