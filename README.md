# 장고 REST Framework를 배워보자!!

```html
나는 아래 장고 REST Framework 사이트 내용을 읽고 따라해보고 읽으며 느낀점을 정리하였다.
```

장고 REST Framework 사이트 주소 → [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

### 1. 장고 REST Framework란?

```html
WEB API 구축을 위한 도구
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

### 2. 장고 REST Framework 설치하기!!

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