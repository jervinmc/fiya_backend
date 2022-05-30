from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import Login
from rest_framework import permissions
from report.views import ReportList,ReportRespo
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/v1/login/', Login.as_view(), name='get_user'),
     path('api/v1/report_list/<str:user_id>/', ReportList.as_view(), name='get_user'),
     path('api/v1/respo_list/<str:report_id>/', ReportRespo.as_view(), name='get_user'),
    
    path('api/v1/users/', include('users.urls')),
    path('api/v1/report/', include('report.urls')),
]