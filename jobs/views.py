from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404,get_list_or_404
from jobs.models import Category, JobsPosting
from rest_framework import viewsets,mixins

from jobs.serializers import CategorySerializers, JobpsotingSerializer, JobsGetSerializer
from mainuser.models import Userprofile
from mainuser.permissions import IsOwnerOrReadOnly
from .mixins import ListModelMixin
from django_filters import rest_framework as filters
from rest_framework_simplejwt.authentication import JWTAuthentication



class JobFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    class Meta:
        model = JobsPosting
        fields = ['category','user']

class GetCategory(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [AllowAny,]
    authentication_classes = [JWTAuthentication]

class JobPosting(viewsets.ModelViewSet):

    queryset = JobsPosting.objects.all()
    serializer_class = JobpsotingSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = JobFilter
        
    def retrieve(self, request, pk=None):
        queryset = JobsPosting.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = JobsGetSerializer(job)
        return Response(serializer.data) 
    def perform_create(self,serializer):
        profile = Userprofile.objects.get(user=self.request.user)
        serializer.is_valid(raise_exception = True)
        serializer.save(user = self.request.user,profile = profile)
        

class personalJobs(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = JobpsotingSerializer
    queryset = JobsPosting.objects.all()
    
    def list(self, request):
        job = get_list_or_404(self.queryset,user = self.request.user)
        serializer = JobpsotingSerializer(job,many = True)
        return Response(serializer.data)


    
