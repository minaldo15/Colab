# Django
1. Django Form
2. Django Model Form
3. Static & Media Files

## Django Form
- 개요
  - Django 서버에 들어오는 요청 중 비정상 혹은 악의적인 요청에 대한 `유효성 검증`이 필요
    - 이러한 유효성 검증은 많은 부가적인 것들을 고려해야 하는데, 생산성을 늦추고 쉽지 않은 작업
  - Django Form은 이 과정에서 과중한 작업과 반복 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만들어 줌
- Form 에 대한 Django의 역할
  - Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
  - Django는 Form과 관련한 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있다.

- Django는 Form에 관련된 작업의 세 부분을 처리
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리

### Django Form Class
- Form Class 선언
  - Model Class 선언과 비슷함
  - Model과 마찬가지로 상속을 통해 선언
  - 앱 폴더에 forms.py를 생성 후 ArticleForm Class 선언
  - form에는 model field와 달리 TextField가 존재하지 않음
- Form rendering options
  1. `as_p()`
  2. as_ul()
  3. as_table()

- Django의 2가지 HTML input 요소 표현
  1. Form fields
   - 입력에 대한 유효성 검사 로직을 처리
   - 템플릿에서 직접 사용됨

  2. Widgets
    - 웹 페이지의 HTML input 요소 렌더링을 담당
      - 단순히 input 요소의 보여지는 부분을 변경
    - Widgets은 반드시 form fields에 할당 됨
    - 
- Widgets
  - Textarea 위젯 적용하기
    - content = forms.CharField(`widget`=forms.Textarea)

## Django Model Form
- ModelForm Class
  - Model 을 통해 Form Class를 만들 수 있는 helper class
  - ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용
- ModelForm 선언
  - forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
  - 정의한 ModelForm 클래스 안에 `Meta 클래스`(fields 혹은 exclude 속성을 사용하여 포함하거나 포함하지 않을 필드를 지정)를 선언
  - 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
  ```python
  class ArticleForm(forms.ModelForm):

      class Meta:
          model = Article
          fields = '__all__'
  ```

## Static files
- Static File
  - 응답할 때 별도의 처리없이 파일내용을 그대로 보여주면 되는 파일
  - 파일 자체가 `고정`되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정되어있음
    - 예를 들어, 웹 사이트는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 추가파일을 제공해야 함
  - Django에서는 이러한 파일들을 "static file"이라 함
    - Django는 staticfiles 앱을 통해 정적파일과 관련된 기능을 제공
- Media File
  - 미디어 파일
  - 사용자가 웹에서 업로드하는 정적파일
  - 유저가 업로드 한 모든 정적파일
- 웹 서버와 정적파일
  - 웹 서버의 기본동작은
    - 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서
    - 응답(HTTP response)을 처리하고 제공하는 것
  - 이는 "자원과 자원에 접근 가능한 주소가 있다."라는 의미
    - 예를 들어, 사진 파일은 자원이고 해당 `사진파일을 얻기 위한 경로인 웹 주소(URL)가 존재함`
  - 즉, 웹 서버는 요청받은 URL로 서버에 존재하는 정적자원(static resource)을 제공함

### Static files 구성하기
- Static files 관련 Settings
  1. STATIC_ROOT
  2. STATICFILES_DIRS
  3. STATIC_URL

1. STATIC_ROOT
  - Default: None
  - Django 프로젝트에서 사용하는 모든 정적파일을 한 곳에 모아 넣은 경로
  - collectstatic이 배포를 위해 정적파일을 수집하는 디렉토리의 절대경로
  - `개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음`
  - 실 서비스 환경(배포 환경)에서 Django의 모든 정적파일을 다른 웹 서버가 직접 제공하기 위해 사용
  - 배포 환경에서는 Django를 직접 실행하는 것이 아니라, 다른 서버에 의해 실행되기 때문에 실행하는 다른 서버는 Django에 내장되어 있는 정적파일들을 인식하지 못함(내장되어 있는 정적 파일들을 밖으로 꺼내는 이유)

2. STATICFILES_DIRS
  - Default:[]
  - app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적파일 경로 목록을 정의하는 리스트
  - 추가 파일 디렉토리에 대한 전체경로를 포함하는 문자열 목록으로 작성되어야 함

3. STATIC_URL
  - Default: None
  - STATIC_ROOT에 있는 정적파일을 참조할 때 사용할 URL
  - 개발 단계에서는 실제 정적파일들이 저장되어 있는 app/static/ 경로 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색
  - `실제 파일이나 디렉토리가 아니며, URL로만 존재`
  - 비어 있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야 함

## Media Files
- ImageField()
  - 이미지 업로드에 사용하는 모델 필드
  - FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용가능
  - 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
  - ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있음

- FileField()
  - FileField(upload_to='', storage=None, max_length=100, **options)
  - 파일 업로드에 사용하는 모델 필드
  - 2개의 선택 인자를 가지고 있음
    1. upload_to
    2. storage

- FileField / ImageField를 사용하기 위한 단계
  1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
  2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정(선택사항)

- MEDIA_ROOT
  - Default:''
  - 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대경로
  - Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
    - 데이터베이스에 저장되는 것은 "파일 경로"
  - MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함

- MEDIA_URL
  - Default:''
  - MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
  - 업로드 된 파일의 주소(URL)를 만들어 주는 역할
    - 웹 서버 사용자가 사용하는 public URL
  - 비어있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야 함