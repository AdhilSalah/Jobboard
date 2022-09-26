
from django.urls import include, path

from jobs.views import GetCategory, JobPosting, personalJobs

from rest_framework.routers import DefaultRouter

app_name = 'jobs'

router = DefaultRouter()
router.register('category',GetCategory,basename='category')
router.register('jobposting',JobPosting,basename='job_posting')
router.register('myjobs',personalJobs,basename='myjobs')

urlpatterns = router.urls