
from django.urls import include, path

from jobs.views import GetCategory, JobPosting

from rest_framework.routers import DefaultRouter

app_name = 'jobs'

router = DefaultRouter()
router.register('category',GetCategory,basename='category')
router.register('jobposting',JobPosting,basename='job_posting')

urlpatterns = router.urls