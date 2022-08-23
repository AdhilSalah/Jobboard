
from dataclasses import fields
from pyexpat import model
from urllib import request
from rest_framework import serializers
from .models import Education, Experience, NewUser, Userprofile



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewUser
        fields=('email','username','password','first_name')
        extra_kwargs={'password':{'write_only':True}}
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance





class SignInSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)




class EducationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Education

        fields =('university','department','remark','start_date','end_date')

        def create(self,validated_data):
            user_edu = Education.objects.create(**validated_data)

            return user_edu
class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Experience

        fields =('company','position','remark_e','start_date_e','end_date_e')

        def create(self,validated_data):
            user_exp = Experience.objects.create(**validated_data)

            return user_exp



class UserProfileCreateSerializer(serializers.ModelSerializer):

    # education = EducationSerializer(required = False)
    # experience = ExperienceSerializer(required = False)


    class Meta:

        model = Userprofile
        fields = ('last_name','date_of_birth','profile_photo','cv','about')   

        def create(self,validated_data):

            
            

            # education_data = validated_data.pop('education')
            # experience_data = validated_data.pop('experience')
            user_profile = Userprofile.objects.create(**validated_data)
            # Education.objects.create(

            #     university = education_data[ 'university'],
            #     department = education_data['department'],
            #     remark = ['remark'],
            #     start_date = ['start_date'],
            #     end_date = ['end_date'],

            # )
            # Experience.objects.create(**experience_data)


            return user_profile





class EducationGetSerializer(serializers.ModelSerializer):

    class Meta:

        model = Education
        fields='__all__'

class ExpeienceGetSerializer(serializers.ModelSerializer):

    class Meta:

        model = Experience
        fields = '__all__' 

class ProfilleGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Userprofile

        fields='__all__'          

        
class UserGetSerializer(serializers.ModelSerializer):

    education = EducationGetSerializer(source = 'user_set',many=True)
    experience = ExpeienceGetSerializer(source = 'ex_user_set',many=True)
    userpro = ProfilleGetSerializer(source= 'pro_user_set')


    class Meta:

        model = NewUser

        fields = ['email','username','first_name','userpro','experience','education']
