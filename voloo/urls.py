from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from voloo.api import views

from rest_framework.authtoken import views as auth_views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', auth_views.obtain_auth_token),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework'))
]
