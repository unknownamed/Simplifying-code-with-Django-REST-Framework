# Django-Girls-tutorial-follow
장고걸스 튜토리얼을 따라하며 블로그를 만들어봅니다.

# 장고를 배워보자!

```jsx
나는 Mac 환경에서 이번에 Django를 배우기로 했다
```

[https://jeffkit.gitbooks.io/django-girls-tutorial/content/ko/](https://jeffkit.gitbooks.io/django-girls-tutorial/content/ko/)

```jsx
나는 이 링크를 통해 장고걸스 튜토리얼을 진행하였다 들어가서 참고하면 좋겠다.
```

### 환경설정 : 파이썬 설치

```jsx
맥 환경에서는 pyenv라는 것을 활용해 폴더마다 파이썬 버전을 바꾸어 개발이 편리한것이 있다는걸 알았다

따라서 홈브루를 통해 pyenv를 설치하며 시작해보겠다
```

터미널을 켜서 입력해보자 → 특정 폴더에서 파이썬 버전을 바꾸고 싶다면 local로 필요버전으로 바꾸자!

```jsx
brew install pyenv # pyenv 설치

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc # 패스설정?
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

pyenv install --list | grep "^\s*3\."  # 버전 목록 확인
pyenv install 3.13.3                    # 최신버전 설치

pyenv global 3.13.3                     # 기본으로 설정

python --version
```

### 시작하기 : 장고걸스 튜토리얼에 관하여

```jsx
나는 장고걸스 튜토리얼이라는 초보자 입문 코스로 진행해 볼겠다. 
나는 장고라는 것이 무엇인지 확실히 모른다 웹을 만들기위한 파이썬을 활용한 웹프레임워크라는 정도만 알고있다. 
이번 튜토리얼을 통해 나는 장고가 무엇인지 알고 기본적인 구조와 문법 가장 간단한 웹을 만들수있는 기초를 얻으면 좋겠다.
시작하겠다.
```

#### 장고걸스 튜토리얼 따라하기

(1. 설치하기. 까지 내용이다.)

1. 가상환경 만들기 → 가상환경을 만들지 않는다면 pip install을 통해 global(내 Mac 전체에)로 장고/파이썬 버전이 통일되어버려서 여러 웹사이트에서 버전을 다르게 쓴다면, 관리가 어렵다
    
    
    따라서 프로젝트 폴더안에 가상환경 폴더를 넣어서 분리시킨다
    
    Example → 폴더 구조 예시
    
    ```jsx
    장고 공부
         |--   내 가상환경 폴더        # 가상환경 (여기 안에 파이썬, pip, 패키지 다 들어있음)
    ```
    
    해보자!  자기 프로젝트 폴더를 하나 만든뒤 그 폴더안에서 터미널을 켜서 시작한다!
    
    ```jsx
    python3 -m venv myvenv #myvenv라는 가상환경을 만든다 -m이 make 만들기 옵션인듯
    
    source myvenv/bin/activate #bin으로 실행파일안에 activate라는 가상환경 실행 버튼이 있는듯(매 터미널을 열때마다 실행해줘야하긴함)
    
    (myvenv) unknownname@MacBookAir ~ % #(myvenv)라는것이 뜨면 성공!!!
    
    pip install django #pip파이썬 패키지 관리자(설치담당)를 통해 장고 설치
    
    deactivate #가상환경 끄기(참고), 잘안씀 터미널창 닫고 다시켜면되서 
    ```
    
    @참고 : 가상머신 vs 가상환경 → 가상머신: 다른 운영체제, 다른 컴퓨터 / 가상환경: 다른 버전(프로그램?), 같은컴퓨터 
    

(2. 인터넷은 어떻게 동작할까요? 까지의 내용이다.)

1. 장고가 하는일에 대하여
    
    밑의 글을 읽고 장고 = 서버에 필요한것(DB에서 정보를 조회하려할때 사람의 쿠키값, 요청에 따라 다른걸 진행한다)이다, 정도로 이해했다.
    
    ```jsx
    장고 튜토리얼을 시작할 때부터, 장고가 무슨 일을 하는지 궁금하셨죠? 
    여러분이 답장을 보낼 때, 모든 사람에게 항상 동일한 내용을 보내고 싶지 않을 거에요. 
    받는 사람에 따라 각각 다른 답장을 보내면 더 좋지 않을까요? 
    이와 같이 장고는 맞춤형 편지를 보낼 수 있도록 도와준답니다. :) -> 장고걸스에 적혀있는 내용을 발췌하였다
    ```
    
2. 내가 누구일까요? Who am i? 입력해보기
    
    whoami라는 명령어를 치면 현재 컴퓨터 사용잔의 이름이 뜬다 → 조금 신기한듯 좋네
    
    ```jsx
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % whoami
    unknownname
    ```
    
3. 경로 확인하기. pwd로 내 현재 위치 알기
    
    ```jsx
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % pwd
    /Users/unknownname/Documents/장고 공부
    ```
    
4. 파일 리스트 보기 → ls 이건 귀찮아서 패스 + 파일 복사 cp 옮길곳파일경로 줄곳파일경로 / 파일 위치 옮기기 mv 옮길곳파일경로 줄곳파일경로
5. 경로 변경 → cd (pwd로 확인한 경로/ ..) 이런거 평소좀 적어서 귀찮아서 패스
    
    ```jsx
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % cd myvenv
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir myvenv % ls
    bin             include         lib             pyvenv.cfg
    
    #참고 myvenv안에는 pyenv로 설치한 파이썬의 설정파일과 가상환경실행때 사용한 bin폴더, 기타 등등이 존재한다
    ```
    
6. 폴더 만들기 → mkdir로 폴더 추가하기(클릭으로 생성하는것도 좋지만 해보는게 좋음)
    
    ```jsx
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % mkdir domakedirectory
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % ls
    domakedirectory myvenv
    
    #참고 아까만들었던 가상환경또한 폴더라 폴더는 2개가 존재한다
    ```
    
7. 폴더 삭제하기
    
    ```jsx
    rm 파일(디렉토리) : 삭제 remove
    rm -r 폴더 : 하위폴더 안 내용물까지 전부 삭제 (재귀적으로, recusive)
    rm -f 폴더 : 확인 없이 강제 삭제 force
    rm -rf 폴더 : 폴더째로 강제 삭제 recusive force
    ```
    
    ```jsx
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir myvenv % cd .. #상대경로 지금위치 바로 위로
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % ls
    domakedirectory myvenv
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % rm -r domakedirectory
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % ls
    myvenv
    ```
    

(3. Command Line 시작하기. 까지 내용이다.)

1. 터미널창 간지나게 닫기 → exit(해커처럼 멋지게 클릭안하고 끄는법이다 → 좀 멋진듯)
    
    ```jsx
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % exit # 당황하지말자 당시은 터미널창을 끈것이다
    
    ```
    

(6. Python 시작하기. 까지 내용이다.)

1. 파이썬 기본 문법 → if의 경우 : 뒤를 비우면 Syntax Error가 발생한다.
    
    ```jsx
    if 3 > 2:    #이것만 적으면 if문이 완결되지않았기에 뭐라도 적어야하는듯
    
    # 실행 시, 오류화면
    $ python3 python_intro.py
    File "python_intro.py", line 2
             ^
    SyntaxError: unexpected EOF while parsing
    
    # --->
     if 3 > 2:
            print('It works!')  #이런식으로 if문을 적었다면 안에 실행문을 무조건 적는것이 문법인듯
    ```
    

11. 장고란?

```jsx
Web Server : http request -> 해당 port에 request가 실제 있는지 확인하는 역할
-> request
Django :  Webserver에서 들고온 request -> Django 내부 unresolver가 URL pattern에 매칭 ->
패턴에 맞는 함수(view)에게 넘김 -> view 함수가 DB 조회,처리 후 response를 생서하여 반환 
-> response
Web browser : Django의 view 함수에게 반환받은 response를 수신함
```

1. 장고 기본 프로젝트 만들기 → 장고 관리자 권한으로 프로젝트를 이 폴더에서 시작함
    
    ```jsx
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % django-admin startproject mysite .
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % ls
    manage.py       mysite          myvenv
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % cd mysite
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir mysite % ls
    __init__.py     asgi.py         settings.py     urls.py         wsgi.py
    ```
    
    ```jsx
    장고 공부
    ├───myvenv #기존에 있던 가상환경
    ├───manage.py #기존에 있던 가상환경 관련 python파일
    └───mysite #새로만들어진 Django 프로젝트 파일
            settings.py
            urls.py
            wsgi.py
            __init__.py
    ```
    
    [manage.py](http://manage.py) → 장고 명령어들을 쓸수있게 만들어 주는 파이썬 파일 (runserver(장고 서버 실행), migrate(DB table 만드는 명령어))
    
    ```python
    #!/usr/bin/env python
    """Django's command-line utility for administrative tasks."""
    import os
    import sys
    
    def main():
        """Run administrative tasks."""
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)
    
    if __name__ == '__main__':
        main()
    ```
    
2. 웹사이트 설정하기
    
    ```python
    mysite/settings.py → 시간대 한국으로 변경하기
    
    + css를 위해 STATIC_ROOT = BASE_DIR / 'static' 추가하기
    ```
    

![image.png](images/image.png)

settings.py

```python
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 6.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p+^&3j*cy__e$7g7e&)18b+5or@mda(tw(3-9&k=%)2=al8!)!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul' #여기를 서울로 바꿔주자!!

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static' # 향후 css를 입히기?위해 여기도 바꿔주자!! 배포할때 파일을 모아두는 위치
```

데이터 베이스 테이블? 만들기

```python
(myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

웹서버 실행하기

```python
(myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 02, 2026 - 18:49:15
Django version 6.0.4, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C. #서버 끄기 컨트롤 c

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
```

![image.png](images/image%201.png)

이 화면이 뜬다면 웹서버는 켜진것이다. 축하한다!! 

1. 블로그 객체 모델링하기
    
    ```python
    Post(블로그 객체)
    --------
    <속성 attribute>
    title(제목)
    text(내용)
    author(작성자)
    created_date(글 작성일)
    published_date(글 게시일)
    
    <행위 method>
    publish()(글 게시하기)
    ```
    
    ```python
    Sqlite(기본 내장 설치 불필요) = 장고의 기본 데이터베이스 어댑터(장고 ↔ **어댑터**(매개체) ↔ 데이터베이스)
    -> 향후 다른 DBMS 설치 가능 (PostgreSQL(psycopg2 설치 필요), MySQL(mysqlclient 설치 필요)
    ```
    
2. 어플리케이션? Application 제작하기
    
    ```python
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % python manage.py startapp blog
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % ls
    blog            db.sqlite3      manage.py       mysite          myvenv
    ```
    
    db.sqlite3는 DB 테이블 인듯 → python manage.py migrate를 통해 만들어진 것으로 보임
    
    blog라는 이름으로 Application이 만들어짐
    
    ```python
    장고 공부
    |-- myvenv    #가상환경
    |-- db.squlite3    #DB 테이블
    ├── mysite   #Django 프로젝트 폴더로 지정
    |       __init__.py
    |       settings.py
    |       urls.py
    |       wsgi.py
    ├── manage.py    #Django 명령어 실행을 위한 python 파일
    └── blog    #Django위에 올려질 블로그 프로그램
        ├── migrations
        |       __init__.py
        ├── __init__.py
        ├── admin.py
        ├── models.py
        ├── tests.py
        └── views.py
    ```
    
    Django에 Application등록하기 → mysite안의 settings.py
    
    ```python
    # Application definition
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog', # 블로그 앱 추가됨!!(마지막 , 붙여도 되고 안붙여도됨/ 붙이는 것이 관례 향후 추가시 용이)
    ]
    ```
    
3. 블로그 객체(클래스) 만들기 
    
    → 모든 Model 객체는 blog라는 폴더 안에 models.py에 선언(적어두기) 해야함
    
    ```python
    from django.db import models
    
    # Create your models here.
    
    from django.utils import timezone # 새롭게 한국 시간대로 설정하기위해 라이브러리 추가
    
    class Post(models.Model):
            author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 외래키 설정, CASCADE(종속)/글 만든 유저 삭제되면 글도 같이 삭제되기
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
    ```
    
    이것을 보면 DB는 PK가 필수라고 배웠는데 여기서는 설정하지 않아 궁금하였다 
    
    [https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types](https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types)공식 문서를 읽어보니
    
    ```python
    모델의 어떤 필드에도 `primary key = True`를 지정하지 않으면 Django는 자동으로 AutoField기본 키를 저장할 `primary key`를 추가합니다.
    ```
    
    라고 하여 Django가 인덱스용 primary key를 만드는것 같다(정확하지 않음)
    
4. Post 클래스 → DB 테이블로 만들기
    
    ```python
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % python manage.py makemigrations blog
    Migrations for 'blog':
      blog/migrations/0001_initial.py
        + Create model Post
    ```
    

(10. Django 모델. 까지의 내용이다.)

1. Django에 Post 테이블 등록해주기
    
    ```python
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % python manage.py migrate blog
    Operations to perform:
      Apply all migrations: blog
    Running migrations:
      Applying blog.0001_initial... OK 
    ```
    
2. Post 테이블 관리하기 → blog/admin.py 파일 내용 추가하기
    
    ```python
    from django.contrib import admin
    
    # Register your models here.
    
    from .models import Post # Post 클래스 가져오기
    
    admin.site.register(Post) #Django의 관리자 페이지에서 Post 클래스를 관리하기 위해 등록하는 과정 -> 슈퍼 유저 계정생성도 필요
    ```
    
    웹 서버 실행 → python manage.py runserver
    
    - 참고 zsh은 z shell(터미널에서 명령어를 입력 받는 프로그램**)**의 약자임
    
    확인하기 → [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
    
    ![image.png](images/image%202.png)
    
    관리할 테이블에 등록 되었다!!
    
    이제 로그인해서 관리해보자!! → 웹 서버가 실행 중이니 다른 터미널 창을 하나 더 키자!!
    
    ```python
    (myvenv) unknownname@hwangdaegyeom-ui-MacBookAir 장고 공부 % python manage.py createsuperuser
    Username (leave blank to use 'unknownname'):admin 
    Email address: ghkdeorua3461@gmail.com
    Password: 
    Password (again): 
    The password is too similar to the username. # 위험하다고한다
    This password is too short. It must contain at least 8 characters. 
    This password is too common.
    Bypass password validation and create user anyway? [y/N]: y #그냥 무시하고 만들자
    Superuser created successfully.
    ```
    
    ![image.png](images/image%203.png)
    
    성공적으로 로그인한 모습이다!!
    
3. 글을 올려보자!! → 장고 관리자 페이지(DB 데이터를 GUI(화면)으로 관리 가능)
    
    ![image.png](images/image%204.png)
    
    ![image.png](images/image%205.png)
    
    글이 올라갔다!!!
    
    게시글에 작성자를 admin을 설정하지 않고 비우니 글이 올라가지 않았다 → 이것을 허용하려면 blog/models.py에서 author에 아래 인자값들을 True로 주어야한다.
    
    ```python
    null=True -> DB에 null 저장 허용
    blank=True -> 폼에서 빈칸 허용
    ```
    
    몇개만 글을 더 올려보자!!
    
    ![image.png](images/image%206.png)
    
4. 나만 볼순 없다!! → 배포하기(GitHub 이용)