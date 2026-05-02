from django.db import models

# Create your models here.

from django.utils import timezone # 새롭게 한국 시간대로 설정하기위해 라이브러리 추가

class Post(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 외래키 설정, 유저 삭제되면 같이 삭제되기
        title = models.CharField(max_length=200) # 글 제목
        text = models.TextField() # 글 내용
        created_date = models.DateTimeField( #글 작성날짜 현재 시간으로 넣기
                default=timezone.now)
        published_date = models.DateTimeField( # 글 게시 날짜 비우기 허용 <- 시스템에서 넣어줘서인가?
                blank=True, null=True)

        def publish(self): # 게시날짜 <- publish 함수 실행시점의 시간으로 넣어주기, 레코드? 정보 저장하기
            self.published_date = timezone.now()
            self.save()

        def __str__(self): #글 제목 주는(반환하는) 함수?
            return self.title