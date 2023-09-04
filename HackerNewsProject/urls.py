from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HackerNews.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
