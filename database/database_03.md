# INDEX
1. A many-to-one relationship
2. N:1 (Comment-Article)
3. N:1 (Article-User)

## N:1 (Comment-Article)
- 개요
  - Comment(N)-Article(1)
  - Comment 모델과 Article 모델 간 관계 설정
  - "0개 이상의 댓글은 1개의 게시글에 작성 될 수 있음"

### 모델 관계 설정
- 게시판의 게시글과 N:1 관계를 나타낼 수 있는 댓글 구현
- N:1 관계에서 댓글을 담당할 Comment 모델은 N, Article 모델은 1이 될 것

### Django Relationship fields
- Django Relationship fields 종류
1. OneToOneField()
   - A one-to-one relationship
2. `ForeignKey()`
   - A many-to-one relationship
3. ManyToManyField()
   - A many-to-many relationship

- ForeignKey(to, on_delete, **options)
  - A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
  - Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
  - 2개의 필수 위치 인자가 필요
    1. 참조하는 `model class`
    2. `on_delete` 옵션

### Comment Model
- Comment 모델 정의
    ```py
    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        content = models.CharField(max_length=200)
        # ~~
        # ~~
        def __str__(self):
            return self.content
    ```
  - 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
  - ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수명(소문자)으로 작성하는 것을 권장 -> `article`   
- ForeignKey arguments - `on_delete`
  - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의
  - 데이터 무결성을 위해서 매우 중요한 설정
  - on_delete 옵션 값
    - `CASCADE`: 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
    - PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들 존재
- Migration 과정 진행
  1. models.py에서 모델에 대한 수정사항이 발생했기 때문에 migration 과정을 진행 -> python manage.py makemigrations
  2. 마이그레이션 파일 0002_comment.py 생성 확인
  3. migrate 진행 -> python manage.py migrate
  - migrate 후 Comment 모델 클래스로 인해 생성된 테이블 확인
  - ForeignKey 모델 필드로 인해 작성된 컬럼의 이름이 `article_id`인 것을 확인
  - 만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성했다면 abcd_id로 만들어짐
    - 이처럼 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장되었던 이유
- 댓글 생성 연습하기
  - shell_plus 실행
  ```
  python manage.py shell_plus
  ```
  1. 댓글 생성
    ```py
    # Comment 클래스의 인스턴스 comment 생성
    comment = Comment()

    # 인스턴스 변수 저장
    comment.content = 'first comment'

    # DB에 댓글 저장
    comment.save()

    # 에러 발생
    django.db ~~~
    # articles_comment 테이블의 ForeignKeyField, article_id 값이 저장시 누락되었기 때문
    
    # 게시글 생성 및 확인
    article = Article.objects.create(title='title', content='content')
    article
    => <Article: title>

    # 외래 키 데이터 입력
    comment.article = article

    # DB에 댓글 저장 및 확인
    comment.save()
    comment
    => <Comment: first comment>
    ```
  2. 댓글 속성 값 확인
    ```py
    comment.pk
    => 1

    comment.content
    => 'first comment'

    # 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
    comment.article
    => <Article: title>

    # article_pk는 존재하지 않는 필드이기 때문에 사용 불가
    comment.article_id
    => 1
    ```
  3. comment 인스턴스를 통한 article 값 접근하기
   ```py
   # 1번 댓글이 작성된 게시물의 pk 조회
   comment.article.pk
   => 1

   # 1번 댓글이 작성된 게시물의 content 조회
   comment.article.content
   => 'content'
   ```
  4. 두번째 댓글 작성해보기
   ```py
   comment = Comment(content='second comment', article=article)
   comment.save()

   comment.pk
   => 2

   comment
   => <Comment: second comment>

   comment.article_id
   => 1
   ```

### 관계 모델 참조
- Related manager
  - Related manager는 N:1 혹은 M:N 관계에서 사용 가능한 문맥
  - Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 `역참조`할 때 사용할 수 있는 manager를 생성
    - 이전에 모델 생성 시 `objects`라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨
- 역참조
  - 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
  - 즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
  - N:1 관계에서는 1이 N을 참조하는 상황
    - 외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조
- ```py
  article.comment_set.method()
  ```
  - Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저
  - article.comment 형식으로는 댓글 객체를 참조할 수 없음
    - 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음
  - 대신 Django가 역참조 할 수 있는 comment_set manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음
    - `N:1 관계에서 생성되는 Related manager의 이름은 참조하는 "모델명_set" 규칙으로 만들어짐`
  - 반면 참조 상황(Comment->Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능

- Related manager 연습
  - shell_plus 실행
  1. 1번 게시글 조회하기
   ```
   article = Article.objects.get(pk=1)
   ```
  2. dir() 함수를 사용해 클래스 객체가 사용할 수 있는 메서드를 확인하기
   ```
   dir(article)
   [
    ...
    'comment_set',
    'content',
    ...
   ]
   ```
  3. 1번 게시글에 작성된 모든 댓글 조회하기(역참조)
   ```
   article.comment_set.all()
   => <QuerySet [<Comment:~~>, <Comment:~~>]>
   ```
  4. 1번 게시글에 작성된 모든 댓글 출력하기
   ```py
   comment = article.comment_set.all()

   for comment in comments:
      print(comment.content)
  ```
- ForeignKey arguments - related_name
  ```py
  # article/models.py
  class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    ...
  ```
  - ForeignKey 클래스의 선택 옵션
  - 역참조시 사용하는 매니저 이름(modle_set manager)을 변경할 수 있음
  - 작성 후, migration 과정이 필요
  - 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 함
  - 작성 후 다시 원래 코드로 복구
    - `위와 같이 변경하면 기존 article.comment_set은 더이상 사용할 수 없고, article.comments 로 대체됨`

- admin site 등록
  - 새로 작성한 Comment 모델을 admin site에 등록하기
  ```py
  from .model import Article, Comment

  admin.site.register(Article)
  admin.site.register(Comment)
  ```

### Comment 구현
### Comment 추가사항

## N:1 (Article-User)
- 개요
  - Article(N)-User(1)
  - Article 모델과 User 모델 간 관계 설정
  - "0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음"

### Referencing the User model
- Django에서 User 모델을 참조하는 방법
  1. settings.AUTH_USER_MODEL
   - 반환 값: 'accounts.User' (문자열)
   - User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용
   - `models.py의 모델 필드에서 User 모델을 참조할 때 사용`
  2. get_user_model()
   - 반환 값: User Object (객체)
   - 현재 활성화(active)된 User 모델을 반환
   - 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User를 반환
   - `models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용`

### 모델 관계 설정
- Article 과 User간 모델 관계 설정
  - Article 모델에 User 모델을 참조하는 외래 키 작성
  ```py
  from django.conf import settings

  class Article(models.Model):
      user = models. ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      ...
  ```
- Migration 진행
  - 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요
  - 첫번째 화면
    - 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
    - 그래서 기본값을 어떻게 작성할 것인지 선택해야 함
    - 1을 입력하고 enter 진행(Provide a one-off default now)
  - 두번째 화면
    - article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
    - 1을 입력하고 enter 진행
    - 그러면 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨
  - migrations 파일 생성 후 migrate 진행

- Django에서 User 모델을 참조하는 방법 정리
  - models.py에서는 settings.AUTH_USER_MODEL
  - 다른 모든 곳에서는 get_user_model()

### CREATE
### DELETE
### UPDATE
### READ
