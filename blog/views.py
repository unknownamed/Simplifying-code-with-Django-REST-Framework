from django.shortcuts import render

# Create your views here.
from .models import Post #다른 models.py에 선언된 Post 클래스 가져오기(동일한 디렉토리는 .py안 붙여도됨)
from django.utils import timezone #now() 함수를 통해 현재시간보다 이전에 게시된 글들을 필터링하기위해

def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        #{'posts' : post} -> key-value 형식으로 'posts'는 템플릿 내에서 쓸 이름이고 posts는 위의 SQL로 조회된 내용이다.
        return render(request, 'blog/post_list.html',  {'posts': posts}) #blog/post_list.html을 렌더함수가 브라우저에 반환해줌
