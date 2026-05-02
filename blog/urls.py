from django.urls import re_path # url 함수 쓰려고 -> url함수 사라짐 -> re_path함수 사용
from . import views # 같은 경로의 views.py에 선언되어있는 post_list사용하려고

urlpatterns = [ #url패턴 -> 정규식으로 추가
    re_path(r'^$', views.post_list, name='post_list'), #post_list라는 view에서 실제 url처리
]