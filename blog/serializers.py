from rest_framework import serializers
from .models import Post


class PostSerializer(
    serializers.ModelSerializer
):  # ModelSerializer로 Json 형식으로 만들어줌
    class Meta:
        model = Post
        fields = ["id", "title", "text", "created_date"]  # Json 형식으로 만들 필드
