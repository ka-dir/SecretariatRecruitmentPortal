from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboards.urls')),
    path('', include('applicantprofiles.urls')),
    path('', include('adverts.urls')),
]
