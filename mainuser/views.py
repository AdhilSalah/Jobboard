
from multiprocessing import context
from unittest import result
from urllib import request, response
from rest_framework.generics import CreateAPIView
from .permissions import IsOwnerOrReadOnly,IsOwnerAcount
from mainuser.models import Education
from .serializers import  EducationGetSerializer, EducationSerializer, ExpeienceGetSerializer, ExperienceSerializer, SignInSerializer, UserCreateSerializer, UserGetSerializer, UserProfileCreateSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import viewsets,mixins
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Experience, NewUser, Userprofile
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.views import exception_handler
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ParseError
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.views import exception_handler



class UserRegistrationView(viewsets.ModelViewSet):
    serializer_class = UserCreateSerializer
    permission_classes = (IsOwnerAcount,)
    queryset = NewUser.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            temp = serializer.validated_data
            serializer.save()
            email = temp.pop('email')
            
            try:
                subject = 'welcome to GFG world'
                message = f'Hi , thank you for registering in geeksforgeeks.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )
            except:
                response = {
                    'message':'email address dot exist'
                }
                return Response(response)    
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)    

    def list(self, request, *args, **kwargs):
        self.permission_classes = (IsAdminUser,)
        return super().list(request, *args, **kwargs)

class signin(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self,request):
        
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request, 
                email=request.data['email'], 
                password=request.data['password'])
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'success':'login success',
                }, status=200)
            else:
                return Response({
                    'message': 'invalid username or password',
                }, status=403)
        else:
            return Response({'message':serializer.errors},status=400)      



    

class CurrentUser(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
            serializer = UserGetSerializer(self.request.user)
            status_code = status.HTTP_200_OK

        

            
            

            
            return Response(serializer.data)





'''
google

client id= 369309222265-m5q6ib5ruoj873hli2hl9fq170u2m678.apps.googleusercontent.com

client secret = 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
'''

#add user profile
# class CreateProfile(APIView):

#     permission_classes=[IsAuthenticated,]
#     serializer_classes = UserProfileCreateSerializer

#     parser_classes = [MultiPartParser,FormParser]
    
#     def post(self,request):
#         print(request.data)
#         serializer = UserProfileCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=self.request.user)

#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:

#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


'''smaple viewsets'''


class UserprofileCreate(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
                    

    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = UserProfileCreateSerializer
    parser_classes = [MultiPartParser,FormParser]
    authentication_classes = [JWTAuthentication]
    queryset = Userprofile.objects.all()


    

    def perform_create(self, serializer):
                try:
                    serializer.save(user=self.request.user)
                except Exception as e:
                    
                    response = {
                        'status':status.HTTP_409_CONFLICT,
                        'message':'user allready have a profile'
                    }

                    raise ParseError(response)
                
                







            

class CreateEducation(viewsets.ModelViewSet):

    permission_classes=[IsAuthenticated,]
    authentication_classes = [JWTAuthentication]
    serializer_class = EducationSerializer
    queryset = Education.objects.all()

    def list(self, request):

        queryset = Education.objects.all()
        blog = get_list_or_404(queryset, user=self.request.user)
        serializer = EducationGetSerializer(blog,many = True) 
        return Response(serializer.data) 


    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        return Response(serializer.data)
#add user experience            


class CreateExperience(viewsets.ModelViewSet):

    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    
    def list(self, request):

        queryset = Experience.objects.all()
        exp = get_list_or_404(queryset, user=self.request.user)
        serializer = ExpeienceGetSerializer(exp,many = True) 
        
        return Response(serializer.data) 


    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        return serializer.data


from rest_framework import permissions
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.views import APIView
import requests



@api_view(["GET"])
@permission_classes([permissions.AllowAny])  
def request_user_activation(request,uid, token):
        """ 
        Intermediate view to activate a user's email. 
        """
        
        post_url = "http://65.2.3.224/auth/users/activation/"
        post_data = {"uid": uid, "token": token}
        
        result = requests.post(post_url, data=post_data)
        content = result.text
        return render(request,'success.html')



from django.shortcuts import redirect, render


def AccountActivate(request,uid,token):

    uid = uid
    token = token
    context = {
        'token':token,
        'uid':uid
    }
    return render(request,'Activate.html',context)


