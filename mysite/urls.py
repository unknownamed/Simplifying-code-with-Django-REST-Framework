"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.urls import re_path, include  # blog 앱에서 url들고오도록 추가
from django.contrib.auth.models import User
from rest_framework import routers, viewsets  # 직렬화 코드 파일 따로 추가
from rest_framework import serializers  # 직렬화 코드 추가


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),  # 관리자 페이지
    path(
        "api/users/", include(router.urls)
    ),  # api/라고만 적으면 blog꺼와 user 2가지 충돌 ->"api/users/"로 구체적으로 바꿈
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/blog/", include("blog.urls")),  # "api/blog/"로 바꿔서 blog용은 따로 만듬
    re_path(r"", include("blog.urls")),
]
