from django.urls import path
from .views import PostList, PostDetail  # APIView 클래스 가져오기

urlpatterns = [
    # 기존 post_list_create 대체, url패턴에 연결된함수 PostList.as_view() - 클래스 하위 함수를 모두 포괄한다는 뜻인듯 로 연결
    path("posts/", PostList.as_view(), name="post-list"),
    # 기존 post_detail_update_delete 대체, url패턴에 함수 연결
    path("posts/<int:pk>/", PostDetail.as_view(), name="post-detail"),
]
