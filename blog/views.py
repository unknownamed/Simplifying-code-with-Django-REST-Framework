from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Post #다른 models.py에 선언된 Post 클래스 가져오기(동일한 디렉토리는 .py안 붙여도됨)
from django.utils import timezone #now() 함수를 통해 현재시간보다 이전에 게시된 글들을 필터링하기위해
from .forms import PostForm #forms.py에 정의된 PostForm 클래스를 import


def post_list(request):
        posts = Post.objects.all().order_by('-published_date')
        #{'posts' : post} -> key-value 형식으로 'posts'는 템플릿 내에서 쓸 이름이고 posts는 위의 SQL로 조회된 내용이다.
        return render(request, 'blog/post_list.html',  {'posts': posts}) #blog/post_list.html을 렌더함수가 브라우저에 반환해줌

def post_detail(request, pk): 
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request): #새 글 작성을 처리하기 위한 view함수 
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
