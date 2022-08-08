
from rest_framework import serializers
from .models import NewUser



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


class UserGetSerializer(serializers.ModelSerializer):

    class Meta:

        model = NewUser

        fields = ['email','username','first_name']



    

    