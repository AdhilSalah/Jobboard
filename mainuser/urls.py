from mainuser import views
from django.urls import include, path
from django.urls import re_path as url
from .views import CurrentUser, UserRegistrationView, signin
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)


urlpatterns = [
    
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin',signin.as_view()),
    url(r'^refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('currentuser/', CurrentUser.as_view(), name="current"),

]
