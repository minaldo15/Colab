# Django
1. Form & Data
2. Django Model
  - Intro
  - Database 맛보기
  - Model 기초
  - Migrations
  - ORM
3. QureySet API

## Form & Data
- Sending and Retrieving form data
  - HTML form element를 통해 사용자와 애플리케이션 간의 상호작용

- Client & Server architecture
  - 웹은 다음과 같이 가장 기본적으로 클라이언트 - 서버 아키텍처를 사용
    - 클라이언트가 서버에 요청을 보내고, 서버는 클라이언트의 요청에 응답
  - 클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
  - 이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공할 수 있음

### Sending form data(Client)
- HTML < form > element
  - 데이터가 전송되는 방법을 정의
  - 웹에서 사용자 정보를 입력하는 여러 방식을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
  - "데이터를 어디(action)로 어떤 방식(method)으로 보낼지"
  - 핵심 속성
    - action
    - method
- HTML form's attributes
  1. action
    - 입력 데이터가 전송될 URL을 지정
    - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 함
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
  2. method
    - 데이터를 어떻게 보낼 것인지 정의
    - 입력 데이터의 HTTP request methods를 지정
    - HTML form 데이터는 오직 2가지 방법으로만 전송할 수 있는데 바로 GET 방식과 POST 방식

- HTML < input > element
  - 사용자로부터 데이터를 입력 받기 위해 사용
  - "type" 속성에 따라 동작 방식이 달라진다.
    - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 각각의 type은 별도로 MDN 문서에서 참고하여 사용하도록 함
    - type을 지정하지 않은 경우, 기본값은 "text"
  - 핵심 속성
    - name
- HTML input's attributes
  - name
    - form을 통해 데이터를 제출했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
    - 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것

- HTTP request methods
  - HTTP
    - HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
  - 예시
    - GET, POST, PUT, DELETE ...
- GET
  - 서버로부터 정보를 조회하는데 사용
    - 즉, 서버에게 리소스를 요청하기 위해 사용
  - 데이터를 가져올 때만 사용해야 함
  - 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
    - 데이터는 URL에 포함되어 서버로 보내짐

- Query String Parameters
  - 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
  - 이러한 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며 기본 URL과 물음표(?)로 구분됨
    - 예시
      - http://~~~~~?key=value&key=value

### Retrieving form data(Server)
- Retrieving form data(Server)
  - 데이터 가져오기(검색하기)
  - 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받음

- Request and Response objects
- 요청과 응답 객체 흐름
  1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
  2. 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
  3. 마지막으로 view 함수는 HttpResponse object를 반환

## Django Model

### Database
- Database
  - 체계화된 데이터의 모임
  - 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
  - 기본 구조
    1. 스키마
    2. 테이블

- 스키마
  - 뼈대
  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
- 테이블
  - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
  - 관계(Relation)라고도 부름
  1. 필드
  2. 레코드

- 필드
  - 속성 혹은 컬럼
  - 각 필드에는 고유한 데이터 형식이 지정됨
    - INT, TEXT 등$$
- 레코드
  - 튜플 혹은 행
  - 테이블의 데이터는 레코드에 저장됨

- PK(Primary Key)
  - 기본 키
  - 각 레코드의 고유한 값(식별자로 사용)
  - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(주민등록번호)
  - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용 됨

- 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어(주로 테이블형 자료구조에서)
  - "Query를 날린다." -> "데이터베이스를 조작한다."

### Model
- 개요
  - Django는 Model을 통해 데이터에 접근하고 조작
  - 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
  - 저장된 데이터베이스의 구조(layout)
  - 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑
    - 모델 클래스 1개 == 데이터베이스 테이블 1개
- Model 작성
  - 모델 클래스를 작성하는 것은 데이터베이스 `테이블의 스키마를 정의`하는 것
  - 모델 클래스 == 테이블 스키마
```python
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```
- Model 이해
  - 각 모델은 django.models.Model 클래스의 서브 클래스
    - 즉, 각 모델은 django.db.models 모듈의 Moedl 클래스를 상속받아 구성됨
    - `클래스 상속 기반 형태의 Django 프레임워크 개발`
  - models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의
    - Article에는 어떤 데이터 구조가 필요한지 정의
    - 클래스 변수 title과 content는 DB 필드를 나타냄
    1. 클래스 변수(속성)명
      - DB 필드의 이름(title, content)
    2. 클래스 변수 값(models 모듈의 Field 클래스)
      - DB 필드의 데이터 타입('=' 오른쪽 부분)

- Django Model Field
  - Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형(INT, TEXT 등)을 정의
  - 데이터 유형에 따라 다양한 모델 필드를 제공
    - DataField(), CharField(), IntegerField() 등

- 데이터베이스 스키마
  - 지금까지 작성한 models.py는 데이터베이스 스키마를 정의한 것
  - 이제 이러한 모델의 변경사항을 실제 데이터베이스에 반영하기 위한 과정이 필요

### Migrations
- 개요
  - Django가 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영하는 방법
- 주요 명령어
  - makemigrations
    - 모델의 변경사항에 대해 새로운 migration을 만들 때 사용
  - migrate
    - makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정
    - 결과적으로 `모델의 변경사항`과 데이터베이스를 동기화
- `migration 3단계`
  1. models.py에서 변경사항이 발생하면
  2. migration 생성
    - makemigrations
  3. DB 반영(모델과 DB의 동기화)
    - migrate

### ORM
- 개요
  - Object-Relational-Mapping
  - 객체 지향 프로그래밍 언어를 사용하며 호환되지 않는 유형의 시스템 간에(Django<->DB) 데이터를 변환하는 프로그래밍 기술
  - Django는 내장 Django ORM을 사용
  - 한마디로 SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체

- ORM 장단점
  - 장점
    - SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
    - 객체 지향적 접근으로 인한 높은 `생산성`
  - 단점
    - ORM 만으로 세밀한 데이터베이스 조작을 구현하기 어려운 경우가 있음

## QureySet API
- 사전준비
  - vscode SQLite 확장프로그램을 통해 직접 테이블 데이터 확인하기
  - 외부 라이브러리 설치 및 설정
    - pip install ipython
    - pip install django-extensions
  - Django shell
    - ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용
    - python manage.py shell_plus
  - 첫 ORM 명령어 사용하기
    - In [1]: Article.objects.all()
    - Out[1]: < QuerySet [] >

- Database API
  - Django가 제공하는 ORM을 사용해 데이터베이스를 조작하는 방법
  - Model을 정의하면 데이터를 만들고 읽고 수정하고 지울 수 있는 API를 제공

- Database API 구문
  - Article.objects.all()
    - Model class/Manager/QureySet API

- objects manager
  - Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
  - Django는 기본적으로 모든 Django 모델 클래스에 대해 objects 라는 Manager 객체를 자동으로 추가함
  - 이 Manager를 통해 특정 데이터를 조작 가능
  - `DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager`

- Query
  - 데이터베이스에 특정한 데이터를 보여 달라는 요청
    - "쿼리문을 작성한다." -> 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
  - 이 때, 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 `QuerySet`이라는 자료 형태로 변환하여 우리에게 전달

- QuerySet
  - 데이터 베이스에게서 전달 받은 객체 목록(데이터 모음)
    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
  - Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음
  - objects manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체
  - 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

### QuerySet API 익히기
- 