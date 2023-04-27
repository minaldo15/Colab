# Vue_01
- INDEX
  - Vue intro
  - Why Vue
  - Vue instance

## Vue intro
- 사전준비 
  - VSCode Vetur extension 설치
    - 문법 하이라이팅, 자동완성, 디버깅 기능 제공
  - Chrome Vue devtools extension 설치 및 설정
    - 크롬 브라우저 개발자 도구에서 vue 디버깅 기능 제공
- 개요
  - Front-end 개발이란 무엇인가
  - Front-end framework란 무엇인가
  - Vue를 배우는 이유
  - Vue 기초 문법

### Front-end Development
- 개요
  - Front-end 개발은 Web App 또는 Web site의 UI/UX를 제작하고 관리하는 과정
  - Front-end 프레임워크와 라이브러리(React, Angular, Vue.js)를 사용하여 개발 효율성을 높이고, Web App의 복잡성을 관리
  - Front-end 개발에 사용되는 주요 기술은 HTML, CSS, JavaScript
- Web App이란
  - 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
  - VIBE 웹 사이트로 이동
  - 개발자 도구 > 디바이스 모드
  - 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것
  - 웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태
- SPA(Single Page Application)
  - Web App과 함께 자주 등장할 용어 SPA
  - 이전까지는 사용자의 요청에 대해 적절한 페이지 별 template을 반환
  - SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
    - 어떻게 한 페이지로 모든 요청에 대응할 수 있을까
    - CSR(Client Side Rendering)방식으로 요청을 처리하기 때문
- SSR(Server Side Rendering)
  - 기존의 요청 처리 방식은 SSR
  - Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
  - 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행
- CSR(Client Side Rendering)
  - 최초 한 장의 HTML을 받아오는 것은 동일
    - 단, server로부터 최초로 받아오는 문서는 빈 html 문서
  - 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링
    1. 필요한 페이지를 서버에 AJAX로 요청
    2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON방식으로 전달
    3. JSON 데이터를 JS로 처리, DOM 트리에 반영(렌더링)
- 왜 CSR 방식을 사용하는가
  1. 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨
     - 클라이언트 - 서버 간 통신 즉, 트래픽 감소
     - 트래픽이 감소한다 = 응답 속도가 빨라진다.
  2. 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
     - SNS에서 추천을 누를 때 마다 첫 페이지로 돌아간다 = 끔찍한 App
     - 요청이 자연스럽게 진행이 된다 = UX 향상
  3. BE와 FE의 작업 영역을 명확히 분리할 수 있음
     - 각자 맡은 역할을 명확히 분리한다 = 협업이 용이해짐
- CSR은 만능인가
  - 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜시간이 소요
  - Naver, Netflix, Disney+ 등 모바일에 설치된 Web-App을 실행하게 되면 잠깐의 로딩시간이 필요
  - `검색 엔진 최적화`가 어려움
    - 서버가 제공하는 것은 텅 빈 HTML
    - 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트(브라우저)가 진행
  - 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움
- CSR vs SSR
  - CCR과 SSR은 흑과 백이 아님
    - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
  - SPA 서비스에서도 SSR을 지원하는 Framework이 발전하고 있음
    - Vue의 Nuxt.js
    - React의 Next.js
    - Angular Universal 등

## Why Vue
- 왜 우리는 vue를 배울까
  - 쉽다.
  - Vue는 타 Framework에 비해 입문자가 시작하기에 좋다.
  - 왜 Vue는 상대적으로 낮은 진입장벽을 갖나
  - Vue를 발표한 개발자 Evan You
    - 구글 Angular 개발자 출신
    - Angular 보다 `가볍고, 간편하게 사용할 수 있는` Framework를 만들기 위해 퇴사
    - 2014년 Vue 발표
- Vue의 기본 구조
  - Vue 구조는 매우 직관적
- Vue 없이 코드 작성하기
  ```
  ```
- Vue CDN
  - Vue로 작업을 시작하기 위하여 CDN을 가져와야 함
  - Django == Python Web Framework
    - pip install
  - Vue === JS Front-end Framework
    - Bootstrap에서 사용하였던 CDN 방식 제공
  - Vue CDN을 위하여 Vue2 공식 문서 참고
    - https://v2.vuejs.org/
    1. Getting Started
    2. Installation
    3. Development version CDN 복사

### Vue 2 vs Vue 3
- Vue3
  - 2022년 02월 부터 Vue 프레임워크의 기본 버전이 3버전으로 전환
  - 대체적인 설정들이 Vue3을 기본으로 적용되어 있음
    - ex) 공식문서, CDN, npm 등
- Vue2
  - 여전히 Vue2가 많이 사용됨
  - 사용된 기간이 긴 만큼 상대적으로 많은 문서의 양, 참고자료, 질문/답변

## Vue instance
- MVVM Pattern
  - 소프트웨어 아키텍처 패턴의 일종
  - 마크업 언어로 구현하는 그래픽 사용자 인터페이스`(view)`의 개발을 Back-end`(model)`로 분리시켜 View가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
  - View - 우리 눈에 보이는 부분 = DOM
  - Model - 실제 데이터 = JSON
  - View Model(Vue)
    - View를 위한 Model
    - View와 연결되어 Action을 주고 받음
    - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
    - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨
- MVVM Pattern 정리
  - MVC 패턴에서 Controller를 제외하고 View Model을 넣은 패턴
  - View는 Model을 모르고, Model도 View를 모른다 == DOM은 Data를 모른다, Data도 DOM을 모른다(독립성 증가, 적은 의존성)
  - View에서 데이터를 변경하면 View Model의 데이터가 변경되고, 연관된 다른 View도 함께 변경된다.
- Vue instance
  1. Vue CDN 가져오기
  2. new 연산자를 사용한 생성자 함수 호출
   - vue instance
  3. 인스턴스 출력 및 확인