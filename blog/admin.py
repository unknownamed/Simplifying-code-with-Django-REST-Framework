from django.contrib import admin

# Register your models here.

from .models import Post # Post 클래스 가져오기

admin.site.register(Post) #Django의 관리자 페이지에서 Post 클래스를 관리하기 위해 등록하는 과정 -> 슈퍼 유저 계정생성도 필요