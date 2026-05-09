# 장고 REST Framework를 배워보자!!

```html
나는 아래 장고 REST Framework 사이트 내용을 읽고 따라해보고 읽으며 느낀점을 정리하였다.
```

장고 REST Framework 사이트 주소 → [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

## 1. 장고 REST Framework란?

```html
Web API 구축을 위한 도구
```

1. 제공 기능
    1. Browsable API 지원 : 웹사이트처럼 테스트 UI를 통해 Json데이터를 확인 지원
    2. [OAuth1a 및](https://www.django-rest-framework.org/api-guide/authentication/#django-rest-framework-oauth) [OAuth2](https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit) 지원 : 로그인 할때, 다른 신뢰할만한 카카오, 구글 등 의 로그인 서비스를 활용한 로그인 지원
    3. [ORM 및](https://www.django-rest-framework.org/api-guide/serializers#modelserializer) [비ORM의](https://www.django-rest-framework.org/api-guide/serializers#serializers) [직렬화](https://www.django-rest-framework.org/api-guide/serializers/) 지원 : 파이썬 객체든 DB객체든 모두 직렬화를 지원함

@참고 → ORM이란?

```html
ORM(Object-Relational Mapping) : 객체 지향 프로그램의 객체와 테이블 형태의 DB를 대응 시켜주는 것
```

@참고 → 400번대 HTTP status code에 대해서…

```html
400 Bad Request : 요청 데이터가 잘못됨(데이터를 넣는 위치나 데이터의 자료형?)
401 Unauthorized : 권한(로그인?) 없어
403 Forbidden : 권한은 있는데 이 권한까지는 없언
404 Not Found : 너가 요청한건 여기는 없어
405 Method Not Allowed : 너의 요청 방식이 틀렸어?(HTTP에서의 GET,PUSH,PUT,DELETE 중 GET HTTP 요청이 아니면 허용하지 않음)
```

@참고 → API vs WEB API, WEB vs Network

```python
API : 프로그램끼리 통신 방법
Web API : HTTP/HTTPS 프로토콜을 활용한 프로그램끼리 통신 방법

Web : HTTP/HTTPS 프로토콜로 통신
Network : Computing unit(연산가능 장치)끼리 통신이 가능한 상태
```

```python
Network(local 네트워크) -> Internet(local 네트워크끼리 연결) -> Web(HTTP를 통한 통신 사용) -> Web API(HTTP로 프로그램끼리 통신 방법)
```

## 2. 장고 REST Framework 설치하기!!

장고 걸스 튜토리얼에서 진행했던곳에서 장고 REST Framework를 설치하여 제공해 주는 기능(직렬화)을 통해 현재 코드에서 어느 부분을 어떻게 간단화 할수있는지 개선해 볼것이다.

pip install을 통해 설치

```html
(myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % pip install djangorestframework 
```

또는

```html
git clone https://github.com/encode/django-rest-framework #이 명령어를 통해 설치할수있다고 한다.
```

mysite/settings.py의 설치된 앱 목록에 추가해서 장고에게 알려주기

```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p+^&3j*cy__e$7g7e&)18b+5or@mda(tw(3-9&k=%)2=al8!)!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ghkdeorua1234.pythonanywhere.com', '127.0.0.1'] #로컬에서 서버 배포했을때를 고려해서 바꿔주기

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'rest_framework', #여기를 추가해주자!!!
]
```

mysite/urls.py ← path("api-auth/", include("rest_framework.urls")) 추가 

→ Django Rest Framework가 제공하는 기능으로, 브라우저 우측 상단에 Log in UI가 생성되어 개발단계에서 계정이 필요한 기능을 테스트할때 용이

```python
from django.contrib import admin
from django.urls import path
from django.urls import re_path, include #blog 앱에서 url들고오도록 추가

urlpatterns = [
    path('admin/', admin.site.urls), #관리자 페이지 URL
    re_path(r'', include('blog.urls')), #blog에서 가져오는 것 추가, r은 정규식 문자때문에 쓰는게 관례(\d, \w)
    path("api-auth/", include("rest_framework.urls")) # Log in UI를 추가하는 REST Framwork에서 제공
]
```

mysite/settings.py ← REST Framework를 통한 사용자 접근 권한 부여

```python
REST_FRAMEWORK = { #REST Framework를 통한 접근권한 간단히 부여 가능 -> 권한 없는 사람 : 읽기만 가능/ 권한 있는 사람 : 쓰기 삭제 가능
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}
```

mysite/urls.py ← 직렬화 코드 추가, ModelViewSet을 통한 CRUD의 간편한 구현 가능, url 패턴 추가

```python
from django.contrib import admin
from django.urls import path
from django.urls import re_path, include #blog 앱에서 url들고오도록 추가
from django.contrib.auth.models import User #Django에 이미 내장으로 정의된 User모델(테이블 스키마 정의)을 가져옴
from rest_framework import routers, serializers, viewsets #REST Framework가 제공하는 라우터, 직렬화, 뷰셋를 가져옴

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer): #User 데이터를 직렬화 하는 코드
    class Meta:
        model = User #User모델을 -> 속성 url, username, email, is_staff(관리자 여부)를 직렬화(DB레코드 -> Json 형식으로 변환)
        fields = ["url", "username", "email", "is_staff"]

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):#CRUD를 ModelViewSet의 상속으로 간단히 구현
    queryset = User.objects.all() #CRUD를 행할 대상 data
    serializer_class = UserSerializer #DB레코드 -> Json data

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter() #라우터라는 URL생성을 담당하는 객체를 만든다.
router.register(r"users", UserViewSet) #users로 시작하는 URL에 CRUD기능을 매칭한다. r은 rawstring(이거 그대로 라는 의미 : users 그대로 넣는다)

urlpatterns = [
    path('admin/', admin.site.urls), #관리자 페이지 URL
    path("api/", include(router.urls)), #api라는 URL이 들어오면 사용자 데이터 CRUD가능
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")), #Browsable API인 우측상단 로그인/로그아웃 버튼 생성
    re_path(r'', include('blog.urls')), #blog에서 가져오는 것 추가, r은 정규식 문자때문에 쓰는게 관례(\d, \w), (정규 표현식 r ''이 빈문자열이라서)포괄적인 기본 주소는 맨밑으로가야됨
]
```

@참고 → Java의 상속은 알고있었지만, 파이썬의 상속 방법을 모르고 있었다. → 파이썬의 경우, class 로 자식 클래스를 정의할때 자식이름(상속받을 부모 이름) 구조로 정의하면 상속이 이루어진다.

```python
# 부모 클래스 정의
class Animal:
    def speak(self):
        print("소리를 냅니다.")

# 자식 클래스가 Animal을 상속받음 (Java의 extends 역할)
class Dog(Animal):
    def bark(self):
        print("멍멍!")
```

@참고 ← router = routers.DefaultRouter() : 라우터를 정의할때, SimpleRouter라는 Django에서 제공하는 다른 방법도 존재한다고 한다.

```python
SimpleRouter : 기능(view 함수?)과 매칭한 URL을 생성.
DefaultRouter : 기능과 매칭한 URL 생성 + router가 연결된 기본 주소(기준 주소 : Base URL**)의** 화면에 사용 가능한 API 주소 목록을 보여줌
```

@참고

**ModelSerializer vs HyperlinkedModelSerializer** ← 튜토리얼에서는 Hyperlinked를 쓰길래 무슨 차이인지 궁금했다.

**ModelSerializer** - DB 객체를 그대로 직렬화

```json
{
    "id": 1,
    "title": "안녕"
}
```

**HyperlinkedModelSerializer** - URL로 표현 ← **REST 원칙 : HATEOAS**(요청에 대한 응답에 추가로 할수있는것을 URL을 통해 사용자는 API 구조를 몰라도 바로 요청 가능)

```json
{
    "url": "http://localhost:8000/posts/1/", #바로 "상세 글"로 갈수있음
    "title": "안녕"
}
```

## 3. 장고 걸스의 Post ← 직렬화를 통해 간단화 해보기

serializers.py ← 직렬화를 활용하기 위해 따로 파일 추가

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer): # ModelSerializer로 자동화 [cite: 164, 169]
    class Meta:
        model = Post # 연결할 모델 [cite: 171]
        fields = ['id', 'title', 'text', 'created_date'] # 보여줄 필드 [cite: 172]
```

## 4. view 함수 단순화하기 ← @api_view 데코레이터

기존 CRUD 작업 담당 → views.py → @api_view 데코레이터로 단순화하기

```python
from rest_framework.decorators import api_view  # 데코레이터를 쓰기 위해 가져옴
from rest_framework.response import Response  # json을 반환하기 위해 가져옴
from rest_framework import status  # 상태코드를 위해 가져옴
from .models import Post  # Post 객체 가져오기
from .serializers import PostSerializer  # json화 된 DB객체를 들고오기 위해 가져옴
from django.shortcuts import get_object_or_404  # 데이터 있으면 들고오고 없으면 404 Not Found표시

# 기존 post_list(목록 조회), post_new(새글 올리기) api_view 데코레이션을 활용한 대체
@api_view(["GET", "POST"])
def post_list_create(request):
    if request.method == "GET":
        posts = Post.objects.all().order_by("-published_date")
        serializer = PostSerializer(
            posts, many=True
        )  # 여러 개일 때, many=True로 모두 직렬화 가능?
        return Response(serializer.data)  # 파이썬 리스트(딕셔너리) -> json으로 만들기

    elif request.method == "POST":
        serializer = PostSerializer(
            data=request.data
        )  # request.POST는 Form태그를 통한 data만 가능 -> Json data를 바꾸기 위해, request.data 사용
        if serializer.is_valid():
            serializer.save(author=request.user)  # 작성자 정보 채워주기
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # 상태코드로 성공을 알려줌
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # 상태코드로 데이터가 잘못되었을경우 client에게 알려줌

# 2. post_detail(상세 글보기), post_edit(기존 글 수정하기) 대응
@api_view(["GET", "PATCH", "DELETE"])
def post_detail_update_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":  # 글 상세 보기
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif (
        request.method == "PATCH"
    ):  # 수정 PUT의 경우 새로 쓰기 때문에 -> 부분 수정에 적합한 PATCH 사용
        serializer = PostSerializer(post, data=request.data, partial=True) # partial=True여야 새로 변경된 필드만 검사함
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":  # 글 삭제
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

@참고 ← 200번대 상태코드

```python
201 CREATED : POST 성공
204 NO CONTENT : DELETE 성공(지워서 데이터 없음)
```

권한 없음 → 읽기 권한만 주기, 권한 있음 → CRUD 권한 다주기

views.py ← @permission_classes 추가

```python
from rest_framework.decorators import (
    api_view,
    permission_classes,
)  # 데코레이터를 쓰기 위해 가져옴
from rest_framework.response import Response  # json을 반환하기 위해 가져옴
from rest_framework import status  # 상태코드를 위해 가져옴
from .models import Post  # Post 객체 가져오기
from .serializers import PostSerializer  # json화 된 DB객체를 들고오기 위해 가져옴
from django.shortcuts import get_object_or_404  # get을 가져오기 위해 가져옴?
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)  # 권한에 따라 읽기 권한을 주거나 CRUD권한 모두 주기

# 기존 post_list(목록 조회), post_new(새글 올리기) api_view 데코레이션을 활용한 대체
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])  # 권한 검사 추가
def post_list_create(request):
    if request.method == "GET":
        posts = Post.objects.all().order_by("-published_date")
        serializer = PostSerializer(
            posts, many=True
        )  # 여러 개일 때, many=True로 모두 직렬화 가능?
        return Response(serializer.data)  # json data 로 돌려주기?

    elif request.method == "POST":
        serializer = PostSerializer(
            data=request.data
        )  # request.POST는 Form태그를 통한 data만 가능 -> Json data를 바꾸기 위해, request.data 사용
        if serializer.is_valid():
            serializer.save(author=request.user)  # 작성자 정보 채워주기
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # 상태코드로 성공을 알려줌
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # 상태코드로 데이터가 잘못되었을경우 client에게 알려줌

# 2. post_detail(상세 글보기), post_edit(기존 글 수정하기) 대응
@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])  # 권한 검사 추가
def post_detail_update_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":  # 글 상세 보기
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif (
        request.method == "PATCH"
    ):  # 수정 PUT의 경우 새로 쓰기 때문에 -> 부분 수정에 적합한 PATCH 사용
        serializer = PostSerializer(
            post, data=request.data, partial=True
        )  # partial=True여야 새로 변경된 필드만 검사함
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":  # 글 삭제
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## 5. Insomnia를 통해 API 응답 확인해보기

Django 서버 켜기

```python
(myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % python manage.py runserver
```

Error 발생 ← 기존 blog/urls.py에 정의된 url 패턴에 현재 view 함수들이 @api_view 데코레이터로 바뀜

blog/urls.py의 url 패턴 → 새로 바뀐 view에 맞게 변경

```python
from django.urls import path
from . import views

urlpatterns = [
    # 1. 기존 post_list, post_new 대체
    path(
        "posts/", views.post_list_create, name="post_list_create"
    ),  # name을 사용해서 코드상에서 편하게 참조가능
    # 2. 기존 post_detail, post_edit 대체
    path(
        "posts/<int:pk>/",
        views.post_detail_update_delete,
        name="post_detail_update_delete",
    ),
]
```

mysite/urls.py의 url 패턴 ← 위의 추가한 User 객체의 url 패턴이 Post 객체의 앞의 api/라는 부분이 동일하여 Post 객체의 url로 못가는 상태 → api/user 와 api/blog 로 구체화하여 구분

```python
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
```

확인해보자! ← Browsable API를 제공하는 Django REST Framework

![image.png](images/image.png)

브라우저 화면으로 상태코드 200 OK와 Json 데이터가 보이는걸 확인할수있다.(Response 함수가 브라우저일 경우, BrowsableAPIRenderer(api_view 데코레이터가 있다면?))

OPTIONS 버튼 눌러보기

![image.png](images/image%201.png)

```python
HTTP 요청 중 하나 : OPTIONS(서버의 기능과 스펙 확인)
OPTIONS 버튼 : API의 사용 설명서

name: API의 이름 -> views.py에 정의된 이름으로 Django REST Framework가 정함
description : API 설명, 파이썬 코드(Docstring)로 설명을 적을수있음(함수 정의의 이름, 바로 아래에 적은 """ """ (Docstring)를 Django REST Framework가 변환)
renders : 서버가 가능한 응답형식
parses : 서버에게 요청 가능한 형식
application/x-www-form-urlencoded / multipart/form-data: HTML 폼(Form) 형식과 파일 업로드 형식 가능blo
```

blog/urls.py ← Docstring 추가하기

```python
# 기존 post_list(목록 조회), post_new(새글 올리기) api_view 데코레이션을 활용한 대체
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])  # 권한 검사 추가
def post_list_create(request): #docstring이라는 optiond요청일때 이것을 보여줌
    """
    블로그 게시글 목록을 조회하거나, 새로운 게시글을 작성하는 API입니다.

    - GET: 전체 게시글 목록을 최신순으로 반환합니다. (누구나 가능)
    - POST: 제목(title)과 내용(text)을 입력받아 새 글을 저장합니다. (로그인 필요)
    """
    if request.method == "GET":
        posts = Post.objects.all().order_by("-published_date")
        serializer = PostSerializer(
            posts, many=True
        )  # 여러 개일 때, many=True로 모두 직렬화 가능?
        return Response(serializer.data)  # json data 로 돌려주기?

    elif request.method == "POST":
        serializer = PostSerializer(
            data=request.data
        )  # request.POST는 Form태그를 통한 data만 가능 -> Json data를 바꾸기 위해, request.data 사용
        if serializer.is_valid():
            serializer.save(author=request.user)  # 작성자 정보 채워주기
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # 상태코드로 성공을 알려줌
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # 상태코드로 데이터가 잘못되었을경우 client에게 알려줌
```

Docstring을 통해 description에 API 설명이 추가된 모습

![image.png](images/image%202.png)

### **Insomnia를 통해 API 응답 확인해보기**

1. GET, URL **:** http://127.0.0.1:8000/api/blog/posts/ 
    
    → 글 전체 목록 보기 성공!!
    

![image.png](images/image%203.png)

1. POST, URL **:** http://127.0.0.1:8000/api/blog/posts/ , Auth → Basic Auth : admin으로 설정 
    
    → 글 생성하기 성공!!
    

![image.png](images/image%204.png)

1. GET, URL **:** http://127.0.0.1:8000/api/blog/posts/10/(방금 생성한 글의 id 10) 
    
    → 글 상세보기 성공!!
    

![image.png](images/image%205.png)

1. PATCH , URL **:** http://127.0.0.1:8000/api/blog/posts/10/ , Auth **:** Basic Auth 설정
    
    → 글 수정, 제목만 수정 성공!!
    

![image.png](images/image%205.png)

1. DELETE , URL **:** http://127.0.0.1:8000/api/blog/posts/10/ , Auth **:** Basic Auth 설정
    
    → 글 삭제 성공!!
    

![image.png](images/image%206.png)

1. 권한에 따라 응답이 다른지 직접 확인하기
    
    Post , URL **:** http://127.0.0.1:8000/api/blog/posts/ , Auth : ****none 설정 
    
    → 실패, 403 Forbidden → 왜 401이 아니라 403일까? 2개의 차이는?
    

![image.png](images/image%207.png)

@참고 → 상태 코드 401 vs 403

```python
401 Unauthorized : 로그인이 되어있지 않음
403 Forbidden : 로그인이 되어있지만, 권한 없음
```

@참고 → Django REST Framework에서 현재 요청에 대한 응답이 401이 아니라 403인 이유

```python
로그인 요청을 보낼수있나? -> 가능 여부에 따라 Django REST Framework는 다른 상태코드르 반환함
Header에 WWW-Authenticate를 넣어서 요청을 보낼수 있을때 : 401 Unauthorized
Header에 WWW-Authenticate를 넣어서 요청을 보낼수 없을떄 : 403 Forbidden

결론 : 현재 서버 설정이 브라우저 세션(session) 기반 인증이라, API 클라이언트(브라우저가 아니라 수동으로 넣지않으면, cookie가 없음)에게는 인증 챌린지(Authentication Challenge)(해결책?)을 줄수 없는 상태
```

mysite/settings.py → 실제 세션 기반 인증인지 확인

```python
REST_FRAMEWORK = { #REST Framework를 통한 접근권한 간단히 부여 가능 -> 권한 없는 사람 : 읽기만 가능/ 권한 있는 사람 : 쓰기 삭제 가능
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
} # DEFAULT_AUTHENTICATION_CLASSES이 빠져있음 -> Django REST Framework가 기본 설정으로 정함

# 기본 설정
'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.SessionAuthentication',  # 세션 방식 인증(위에 적힌것 먼저 검사)
	    'rest_framework.authentication.BasicAuthentication', # Header에 id 비번 값 -> 암호화 BASE 64방식으로 한것을 넣음
],
```

## 6. @api_view로 구현한 view함수 ← APIView 클래스 활용 간단화

blog/views.py 수정

```python
from rest_framework.views import APIView #APIView 클래스 가져오기
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer

# 1. post_list_create 대체
class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # 권한설정 변수값 Django REST Framework는 리스트 객체로 받아야함(내부적으로 반복문(반복가능한 객체여야함)으로 처리)

    def get(self, request): # 클래스 내 함수는 self(다른이름가능)라는 자기 클래스의 객체를 넣는곳 필요(클래스의 객체가 들어가는 자리 -> 객체.함수() -> 함수(객체)로 파이썬이 실행한다.) 
        posts = Post.objects.all().order_by("-published_date")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. post_detail_update_delete 대체
class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        # 중복 코드를 줄이기 위해 객체를 가져오는 함수를 따로 뺍니다.
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist: # 해당 pk의 객체가 없으면 아무것도 반환하지않음
            return None #null과 같은 개념?

    def get(self, request, pk):
        post = self.get_object(pk) #self를 통해 다른 함수에서 클래스내 정의된 get_object함수를 불러올수있음        if post is None: #해당 pk의 객체가 없으면 404를 반환
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def patch(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

```

blog/urls.py 수정

```python
from django.urls import path
from .views import PostList, PostDetail  # APIView 클래스 가져오기

urlpatterns = [
    # 기존 post_list_create 대체, url패턴에 연결된함수 PostList.as_view() - 클래스 하위 함수를 모두 포괄한다는 뜻인듯 로 연결
    path("posts/", PostList.as_view(), name="post-list"),
    # 기존 post_detail_update_delete 대체, url패턴에 함수 연결
    path("posts/<int:pk>/", PostDetail.as_view(), name="post-detail"),
]
```

## 7.  APIView 클래스로 구현한 view함수 **Insomnia로 테스트하기**

위의 Insomnia 테스트 결과와 동일한것을 확인했다.

## 8. 진행하면서 어려웠던 부분 → 해결 방법

### 어려웠던 부분 : Django 서버를 막상 켜니 → Error 발생 + 동일한 “api/”라는 url 패턴으로 시작하여 User 객체를 처리하는 부분에게 넘겨져서 Post객체를 처리하지 못함

```python
(myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % python manage.py runserver
```

### 해결 방법 :

1. Error 해결방법 → url 패턴을 바뀐 @api_view 데코레이터에 맞게 변경

blog/urls.py의 url 패턴 → 새로 바뀐 view에 맞게 변경

```python
from django.urls import path
from . import views

urlpatterns = [
    # 1. 기존 post_list, post_new 대체
    path(
        "posts/", views.post_list_create, name="post_list_create"
    ),  # name을 사용해서 코드상에서 편하게 참조가능
    # 2. 기존 post_detail, post_edit 대체
    path(
        "posts/<int:pk>/",
        views.post_detail_update_delete,
        name="post_detail_update_delete",
    ),
]
```

1. 동일한 “api/”라는 url 패턴으로 시작하여 User 객체를 처리하는 부분에게 넘겨져서 Post객체를 처리하지 못함 → api/user 와 api/blog 로 구체화하여 구분

mysite/urls.py의 url 패턴 ← 위의 추가한 User 객체의 url 패턴이 Post 객체의 앞의 api/라는 부분이 동일하여 Post 객체의 url로 못가는 상태 → api/user 와 api/blog 로 구체화하여 구분

```python
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
```

## 후기

```python
장고걸스 튜토리얼의 경우, 그대로 따라하면 되기에 비교적 수월하였지만 
→ 장고걸스 튜토리얼에서 진행했던 Blog 위에 Django REST Framework를 활용해서 기존 코드를 변경하는 것은 많은 고려사항이 따른다는 것을 직접 느꼈다.
```