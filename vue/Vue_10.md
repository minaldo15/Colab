# Vue_11
- INDEX
  - DRF Auth System
  - DRF Auth with Vue
## DRF Auth System
### Authentication & Authorization
- Authentication - 인증, 입증
  - 자신이라고 주장하는 사용자가 누구인지 확인하는 행위
  - 모든 보안 프로세스의 첫 번째 단계(가장 기본 요소)
  - 즉, 내가 누구인지를 확인하는 과정
  - 401 Unauthorized
    - 비록 HTTP 표준에서는 "미승인(unauthorized)"을 명확히 하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미
- Authorization - 권한 부여, 허가
  - 사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정(절차)
  - 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
    - 사용자는 조직에 대한 액세스 권한을 부여 받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야 함
  - 서류의 등급, 웹 페이지에서 글을 조회 & 삭제 & 수정할 수 있는 방법, 제한 구역
    - 인증이 되었어도 모든 권한을 부여 받는 것은 아님
  - 403 Forbidden
    - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음
- Authentication & Authorization work together
  - 회원가입 후, 로그인 시 서비스르 이용 할 수 있는 권한 생성
    - 인증 이후에 권한이 따라오는 경우가 많음
  - 단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 것은 아님
    - Django에서 로그인을 했더라도 다른 사람의 글까지 수정/삭제가 가능하진 않음
  - 세션, 토큰, 제 3자를 활용하는 등의 다양한 인증 방식이 존재

### Authentication determined
- 인증 여부 확인 방법
  - DRF 공식문서에서 제안하는 인증 절차 방법
    - https://www.django-rest-framework.org/api-guide/authentication/
  - settings.py에 작성하여야 할 설정
    - "기본적인 인증 절차를 어떠한 방식으로 둘 것이냐"를 설정하는 것
    - 예시의 2가지 방법 외에도 각 framework마다 다양한 인증 방식이 있음
  - 우리가 사용할 방법은 DRF가 기본으로 제공해주는 인증 방식 중 하나인 TokenAuthentication
  - 모든 상황에 대한 인증 방식을 정의하는 것이므로, 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식이 필요
  - view 함수마다(각 요청마다) 다른 인증 방식을 설정하고자 한다면 decorator 활용
- 다양한 인증 방식
  - BasicAuthentication
    - 가장 기본적인 수준의 인증 방식
    - 테스트에 적함
  - SessionAuthentication
    - Django에서 사용하였던 session 기반의 인증 시스템
    - DRF와 Django의 session인증 방식은 보안적인 측면을 구성하는 방법에 차이가 있음
  - RemoteUserAuthentication
    - Django의 Remote user 방식을 사용할 때 활용하는 인증 방식
  - TokenAuthentication
    - 매우 간단하게 구현할 수 있음
    - 기본적인 보안기능 제공
    - 다양한 외부 패키지가 있음
  - (중요) settings.py에서 DEFAULT_AUTHENTICATION_CLASSES를 정의
    - TokenAuthentication 인증 방식을 사용할 것임을 명시
- TokenAuthentication 사용 방법
  - INSTALLED_APPS에 `rest_framework.authtoken` 등록
  - 각 User 마다 고유 Token 생성
  - 생성한 Token을 각 User에게 발급
    - User는 발급 받은 Token을 요청과 함께 전송
    - Token을 통해 User 인증 및 권한 확인
  - Token 발급 방법
    ```py
    def some_view_func(request):
        token = Token.objects.create(user=...)
        return Response({'token': token.key})
    ```
  - User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
    - 단, 반드시 Token 문자열 함께 삽입
      - 삽입해야 할 문자열은 각 인증 방식마다 다름
    - 주의) Token 문자열과 발급받은 실제 token 사이를 ''(공백)으로 구분
  - Authorization HTTP headers 작성 방법
    ```
    Authorization: Token 994...b
    ```

### dj-rest-auth
- dj-rest-auth
  - 회원가입, 인증(소셜미디어 인증 포함), 비밀번호 재설정, 사용자 세부정보 검색, 회원정보 수정 등을 위한 REST API end point 제공
  - 주의) django-rest-auth는 더 이상 업데이트를 지원하지 않음 `dj-rest-auth` 사용
    - https://github.com/iMerica/dj-rest-auth
- dj-rest-auth 사용 방법
  1. 패키지 설치
    - pip install dj-rest-auth
  2. App 등록
    - INSTALLED_APPS에 dj_rest_auth 추가
  3. url 등록
    - urlpatterns에 path('dj-rest-auth/', include('dj_rest_auth.urls')) 추가



