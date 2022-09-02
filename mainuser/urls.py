from atexit import register
from mainuser import views
from django.urls import include, path
from rest_framework import routers
from django.urls import re_path as url

from mainuser.models import Userprofile
from .views import CreateEducation, CreateExperience,CurrentUser, RedirectSocial, UserRegistrationView, UserprofileCreate, signin
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register('signup',UserRegistrationView,basename = 'userregistration')
router.register('profile/createprofile',UserprofileCreate,basename='createprofile-1')
router.register('profile/education',CreateEducation,basename='education')
router.register('profile/experience',CreateExperience,basename='experience')
urlpatterns = [
    
    # url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin',signin.as_view()),
    url(r'^refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('currentuser/', CurrentUser.as_view(), name="current"),
    
    path('get_profile/', RedirectSocial.as_view()),
    
    # path('profile/createprofile/',CreateProfile.as_view(),name='createprofile'),
    # path('profile/createeducation/',CreateEducation.as_view(),name='education'),
    # path('profile/createexperience/',CreateExperience.as_view(),name='experiencec'),zz
    
    
    

]
urlpatterns += router.urls

'''
/auth/token/    ---- for authentication
/auth/convert-token ------for social auth

/auth/revoke-token ------userlogout
'''
