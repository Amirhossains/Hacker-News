from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('', include('HackerNews.urls')),
    path('', include('News.urls')),
    path('', include('EmailDigest.urls')),
    path('', include('Django.urls'))
]
