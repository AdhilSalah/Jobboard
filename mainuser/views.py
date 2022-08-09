from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from .serializers import EducationSerializer, ExperienceSerializer, SignInSerializer, UserCreateSerializer, UserGetSerializer, UserProfileCreateSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.parsers import MultiPartParser,FormParser
from django.views.decorators.csrf import csrf_exempt





class UserRegistrationView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED

        response = {
                    'success' : 'True',
                    'status code' : status_code,
                    'message': 'User registered  successfully',
                    }
                
        return Response(response, status=status_code)


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
            return Response({'message':serializer.errors}, status=400)      


'''for  auth you must provide
{
 "client_id":"lesL0tHw2VuxWdqczKeSEouvCaTlDKWXN5kqeWB8",
 "client_secret":"ExrRhhu3sPsnzNLLRfY3Ly4b3tQky4Hy4ocJqLkKHvh9i4CyfpciG6fwPDQAA2zHD9jyhdmjbLHe22WzLtF9XEjNr2y2bvINvPPFX6YQ13cEUMOs1vJJMtJCaR3MNKDz",
 "grant_type":"password",
 "username":"adhilsalah06@gmail.com",
 "password":"123"
}

for refresh token


"client_id":"7eHbIvcIBsGKD3mb0P4C1OHu1RrSnsLzlHvuaUu9",
"client_secret":"Ehes1gWXMKLO4gFUrQtYWSHsz8iXpBTLk86568r7RVpvybln2m9gyoNzt9aM5ew2SKC0mcZ0FyyxZ75UT0FwdYD84Q0xQ0ditJOjV97y9IpKagrCfbtLyw8eeWuQxbrh",
"grant_type":"refresh_token",
"refresh_token":"token",


'''     

class CurrentUser(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
            serializer = UserGetSerializer(self.request.user)
            return Response(serializer.data)



'''
google

client id= 369309222265-m5q6ib5ruoj873hli2hl9fq170u2m678.apps.googleusercontent.com

client secret = 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
'''

#add user profile
class CreateProfile(APIView):

    permission_classes=[IsAuthenticated,]

    parser_classes = [MultiPartParser,FormParser]
    
    def post(self,request):
        print(request.data)
        serializer = UserProfileCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#add user education            

class CreateEducation(APIView):

    permission_classes=[IsAuthenticated,]


    
    def post(self,request):
        print(request.data)
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#add user experience            


class CreateExperience(APIView):

    permission_classes=[IsAuthenticated,]

    
    
    def post(self,request):
        print(request.data)
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)                        



