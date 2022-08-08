from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from .serializers import SignInSerializer, UserCreateSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth import authenticate





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
