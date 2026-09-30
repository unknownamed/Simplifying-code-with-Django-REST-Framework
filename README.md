# Django Blog REST API · APIView

**Django 블로그를 JSON 기반 API로 바꾸며 직렬화, 요청 처리, 인증 권한을 학습한 프로젝트입니다.**

함수형 API 뷰에서 `APIView`로 코드를 정리한 과정과 Insomnia 요청·응답 기록을 담았습니다.

`Python` · `Django 6.0.4` · `Django REST Framework` · `SQLite` · `Insomnia`

[전체 구현 기록](docs/learning-notes.md) · [이전: Django 블로그](https://github.com/unknownamed/Django-Girls-tutorial-follow) · [다음: ViewSet 리팩터링](https://github.com/unknownamed/Django-REST-Framework-Refactoring)

## 요청·응답 미리보기

<img src="images/image%203.png" alt="Insomnia에서 게시글 목록을 조회한 기존 실행 화면" width="760">

> 게시글 목록 조회의 기존 실행 화면입니다. 상세 요청·응답은 구현 기록에 보존했습니다.

## API 구성

기본 URL: `http://127.0.0.1:8000/api/blog`

| 메서드 | 경로 | 처리 |
| --- | --- | --- |
| GET | `/posts/` | 전체 글 목록 |
| POST | `/posts/` | 새 글 생성 핸들러 |
| GET | `/posts/<pk>/` | 글 상세, 없는 글은 404 |
| PATCH | `/posts/<pk>/` | 전달한 필드만 수정 |
| DELETE | `/posts/<pk>/` | 삭제, 성공 시 204 |

동일한 게시글 API가 `/posts/`에도 연결되어 있습니다. 응답 필드는 `id`, `title`, `text`, `created_date`이며, 조회는 비로그인 상태에서도 가능합니다. 쓰기 요청에는 인증이 필요합니다.

### 현재 코드의 제약

POST 핸들러는 `serializer.save()`를 호출하지만, 필수 필드인 `author`를 지정하지 않습니다. 새 글 생성은 이 부분의 보완이 필요하며, 현재 상태 확인에는 관리자에서 만든 글의 조회·수정·삭제를 사용합니다. 작성자별 수정·삭제 권한도 별도로 구현되어 있지 않습니다.

## 로컬 실행

Python 3.12 이상을 사용합니다. 저장소에 의존성 고정 파일이 없으므로 아래는 현재 코드의 Django 버전에 맞춘 설치 예시입니다.

```bash
python -m venv .venv
```

Windows PowerShell은 `.\.venv\Scripts\Activate.ps1`, macOS/Linux는 `source .venv/bin/activate`로 가상환경을 활성화한 뒤 실행합니다.

```bash
python -m pip install "Django==6.0.4" djangorestframework
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

관리자 화면 `http://127.0.0.1:8000/admin/`에서 사용자를 만들거나 게시글을 준비합니다. 브라우저 API 화면에서는 `/api-auth/login/`으로 로그인하고, API 클라이언트에서는 인증 정보를 설정합니다.

## 요청 예시

```bash
curl http://127.0.0.1:8000/api/blog/posts/
```

인증된 API 클라이언트에서 기존 글을 수정할 때의 본문:

```json
{
  "title": "수정한 제목"
}
```

## 코드 읽는 순서

1. [모델](blog/models.py): 블로그 게시글 데이터
2. [Serializer](blog/serializers.py): API로 전달할 필드와 검증
3. [APIView](blog/views.py): 메서드별 요청·응답 처리
4. [앱 URL](blog/urls.py) / [프로젝트 URL](mysite/urls.py): 경로 연결

## 학습 기록

[기존 설명·코드·실행 화면 전체 보기](docs/learning-notes.md)
