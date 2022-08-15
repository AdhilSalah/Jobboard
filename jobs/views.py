from mmap import PAGESIZE
import profile
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

from rest_framework.generics import RetrieveAPIView,ListCreateAPIView
from jobs.models import Category, JobsPosting
from rest_framework import viewsets,mixins

from jobs.serializers import CategorySerializers, JobpsotingSerializer, JobsGetSerializer
from mainuser.models import Userprofile
from rest_framework.pagination import PageNumberPagination,CursorPagination
from .mixins import ListModelMixin

class GetCategory(viewsets.ModelViewSet):

    queryset = Category.objects.all()

    serializer_class = CategorySerializers
    permission_classes = [AllowAny,]



class JobPosting(viewsets.ModelViewSet):

    queryset = JobsPosting.objects.all()
    

    serializer_class = JobpsotingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def list(self, request):
        
        queryset = JobsPosting.objects.all()
        page = self.paginate_queryset(queryset)
        
        serializer = JobsGetSerializer(page,many = True)
        return self.get_paginated_response(serializer.data)
        
    def retrieve(self, request, pk=None):
        queryset = JobsPosting.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = JobsGetSerializer(job)
        return Response(serializer.data) 
    def perform_create(self,serializer):
        profile = Userprofile.objects.get(user=self.request.user)
        serializer.is_valid(raise_exception = True)
        serializer.save(user = self.request.user,profile = profile)
        

        


    
