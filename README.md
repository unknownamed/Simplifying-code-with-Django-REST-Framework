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
    2. [OAuth1a 및](https://www.django-rest-framework.org/api-guide/authentication/#django-rest-framework-oauth) [OAuth2](https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit) 지원 : 로그인 할때, 다른 신뢰할만한 카카오, 구글의 로그인 서비스를 활용한 로그인 지원
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