# APIView 실행 GIF

Python 3.12, Django 6.0.4, Django REST Framework 3.18.1로 저장소의 Django 코드를 실행했습니다. GIF는 실제 HTTP 요청·응답·상태 코드를 1280×720 프레임에 배치한 기록입니다.

## 실행 환경

캡처에는 원본 코드의 별도 복사본과 새 SQLite DB를 사용했습니다. 원본 소스와 저장소의 기존 DB는 변경하지 않았습니다. 로컬 데모 사용자로 Basic 인증을 적용했으며 인증 정보는 GIF에 포함하지 않았습니다.

```bash
python -m pip install "Django==6.0.4" "djangorestframework==3.18.1"
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:18081
```

현재 POST는 필수 작성자를 저장하지 않으므로, 새 데모 글 한 개를 Django 모델로 준비한 뒤 조회·수정·삭제 요청을 보냈습니다. 직접 재현할 때는 관리자 화면에서 데모 글을 먼저 만들 수 있습니다.

## 확인한 요청

| 순서 | 요청 | 실제 응답 |
| --- | --- | --- |
| 1 | GET `/api/blog/posts/` | 200, 준비한 글 1개 |
| 2 | GET `/api/blog/posts/{id}/` | 200, 글 상세 |
| 3 | PATCH `/api/blog/posts/{id}/` | 200, 제목 `Updated title` |
| 4 | GET `/api/blog/posts/{id}/` | 200, 변경한 제목 확인 |
| 5 | DELETE `/api/blog/posts/{id}/` | 204, 본문 없음 |
| 6 | GET `/api/blog/posts/` | 200, 빈 배열 |

수정 본문은 `{"title": "Updated title"}`입니다. 조회·수정·삭제 결과를 실제 응답으로 확인했으며 생성 API를 실행한 것처럼 표시하지 않았습니다.
