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
from django.urls import re_path, include #blog 앱에서 url들고오도록 추가

urlpatterns = [
    path('admin/', admin.site.urls), #관리자 페이지 URL
    re_path(r'', include('blog.urls')), #blog에서 가져오는 것 추가, r은 정규식 문자때문에 쓰는게 관례(\d, \w)
]
