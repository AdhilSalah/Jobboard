"""jobboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


from jobboard.views import RedirectSocial
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('auth/',include('rest_framework.urls')),
    # path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path("auth1/", include("mainuser.urls")), 
    path('auth/',include('rest_framework.urls')),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('auth/', include('djoser.social.urls')),
    

    path('jobs/',include('jobs.urls')),
    path('blog/',include('blogs1.urls')),
    path('chat/',include('chat.urls')),
    path('docs/', include_docs_urls(title='BlogAPI')),
    path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0"
    ), name='openapi-schema'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
