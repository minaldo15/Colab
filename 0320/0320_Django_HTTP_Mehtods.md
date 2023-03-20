# Django
1. Admin Site
2. CRUD with View
- 사전 준비
- Read & Create
- HTTP Methods
- Delete & Update
- Handling HTTP requests

## Admin site
- 개요
  - Django의 가장 강력한 기능 중 하나인 automatic admin interface
  - "관리자 페이지"
    - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
    - 모델 class를 admin.py에 등록하고 관리
    - 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있음

- admin 계정 생성
  - python manage.py createsuperuser
  - username과 password를 입력해 관리자 계정을 생성

- admin site 로그인
  - http://127.0.0.1:8000/admin/ 로 접속 후 로그인
  - 계정만 만든 경우 Django 관리자 화면에서 모델 클래스는 보이지 않음

- admin에 모델 클래스 등록
  - 모델의 record를 보기 위해서는 admmin.py에 등록 필요

- 데이터 CRUD 테스트
  - admin 페이지에서 데이터 조작해보기

## CRUD with View functions
- 개요  
  - 이전에 익힌 QuerySet API를 통해 view 함수에서 직접 CRUD 구현하기

### 사전준비
- base 템플릿 작성
  - bootstrap CDN 및 템플릿 추가 경로 작성
- url 분리 및 연결
- index 페이지 작성(urls, views, html)
- Article Model 작성

### READ 1(index page)
- 전체 게시글 조회
  - index 함수에 articles = Article.objects.all() / context = {`'articles'`:articles,} 추가

### READ 2(detail page)
- 개요
  - 개별 게시글 상세 페이지 제작
  - 모든 게시글 마다 뷰 함수와 템플릿 파일을 만들 수는 없음
    - 글의 번호(pk)를 활용해서 하나의 뷰 함수와 템플릿 파일로 대응
  - Variable Routing 활용
- urls
  - URL로 특정 게시글을 조회할 수 있는 번호를 받음
  - path(`'< int:pk >/'`, views.detail, name='detail')
- views
  - Article.objects.get(pk(id)=pk)에서 오른쪽 pk는 variable routing을 통해 받은 pk, 왼쪽 pk는 DB에 저장된 레코드의 id 컬럼
- templates
  - 제목을 누르면 상세 페이지로 이동
  - < a href="{% url `'articles:detail'` `article.pk` %}">< p>글 제목: `{{article.title}}`< /p>< /a>

### CREATE
- 개요
  - Create 로직을 구현하기 위해서는 2개의 view 함수가 필요
    - 사용자의 입력을 받을 페이지를 렌더링 하는 함수 1개
      - `"new"` view function
    - 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수 1개
      - `"create"` view function
- New
  - urls, views, html
  - new.html
    - ```html 
      {% block content %}
      <h1>NEW</h1>
      <form action="{% url 'articles:create' %}" method="GET">
        <label ~~~>
        <input ~~~>
        <label ~~~>
        <textarea ~~~>
        <input type="submit">
      </form>
      <a href="{% url 'articles:index' %}">[back]</a>
      {% endblock content %}
      ```

- Create
  - view
    - ```python 
      def create(request):
          title = request.GET.get('title')
          content = request.GET.get('content')

          # 1.
          # article = Article()
          # article.title = title
          # article.content = content
          # article.save()

          # 2.
          # article = Article(title=title, content=content)
          # articl.save()

          # 3.
          Article.objects.create(title=title, content=content)

          return redirect('articles:detail', article.pk)
      ```
    - 1 또는 2번째 생성 방식을 사용하는 이유
      - create 메서드가 더 간단해 보이지만 추후 데이터가 저장되기 전에 유효성 검사 과정을 거치게 될 예정
      - 유효성 검사가 진행된 후에 save 메서드가 호출되는 구조를 택하기 위함
  - Django shortcut function - "redirect()"
    - 인자에 작성된 곳으로 다시 요청을 보냄
    - 사용 가능한 인자
      1. view name(URL pattern name) - `'articles:index'`
      2. absolute or relative URL - `'/articles/'`
        
### HTTP Method        

