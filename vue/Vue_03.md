# Vue_03
- INDEX
  - Vue cli
  - SFC

## Vue CLI
- Vue CLI
  - Vue 개발을 위한 표준 도구
  - 프로젝트의 구성을 도와주는 역할
  - 확장 플러그인, GUI, Babel등 다양한 tool 제공
- Vue CLI Quick Start
  - 설치
  ```
  npm install -g @vue/cli
  ```
  - 프로젝트 생성
  ```
  vue create 프로젝트 이름
  ```
  - Vue 버전 선택
  ```
  Default ([Vue 2] babel, eslint)
  ```
  - 출력된 명령어 실행
    - 프로젝트 디렉토리로 이동
    ```
    cd 폴더 이름
    ```
    - 프로젝트 실행
    ```
    npm run serve
    ```
  - 주소 ctrl + 클릭
  - 프로젝트 메인 페이지
### Vue CLI 프로젝트 구조
- node_modules
  - node.js 환경의 여러 의존성 모듈
  - python의 venv와 비슷한 역할을 함
    - 따라서 .gitignore에 넣어주어야 하며, Vue 프로젝트를 생성하면 자동으로 추가됨
- node_modules - `Babel`
  - "JavaScript compiler"
  - 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
  - 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
    - 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생
    - 버전에 따른 같은 의미의 다른코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구
    - 원시 코드(최신 버전)를 목적 코드(구 버전)로 옮기는 번역기가 등장하면서 더 이상 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있음
- node_modules - `Webpack`
  - "static module bundler"
  - 모듈 간의 의존성 문제를 해결하기 위한 도구
  - 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
- Module
  - 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
  - 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 모듈 즉, js파일 하나가 하나의 모듈
  - 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
  - 여러 모듈 시스템
    - ESM(ECMA Script Module), AMD, CommonJS, UMD
- Module 의존성 문제
  - 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
    - Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장
- Bundler
  - 모듈 의존성 문제를 해결해주는 작업이 Bundling
  - 이러한 일을 해주는 도구가 Bundler이고, Webpack은 다양한 Bundler 중 하나
  - 모듈을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 만들어짐
  - Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지않고 동작하게 됨
  - snowpack, parcel, rollup.js 등의 webpack 이외에도 다양한 모듈 번들러 존재
  - `Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음`
- package.json
  - 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함
- package-lock.json
  - node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
  - 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
  - 사용할 패키지의 버전을 고정
  - 개발 과정 간의 의존성 패키지 충돌 방지
  - python의 requirements.txt 역할
- public/index.html
  - Vue 앱의 뼈대가 되는 html 파일
  - Vue 앱과 연결될 요소가 있음
- src
  - src/assets
    - 정적 파일을 저장하는 디렉토리
  - src/components
    - 하위 컴포넌트들이 위치
  - src/App.vue
    - 최상위 컴포넌트
    - public/index.html과 연결됨
  - src/main.js
    - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
    - public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳
    - Vue 전역에서 활용할 모듈을 등록할 수 있는 파일
## Component
- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  - 즉, 기능별로 분화한 코드 조각
- CS에서 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
  - Body tag를 root node로 하는 tree의 구조이다
  - 마찬가지로, Vue에서는 src/App.vue를 root node로 하는 tree의 구조를 가짐
- 컴포넌트는 유지보수를 쉽게 만들어줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공
- Component based architecture 특징
  - 관리가 용이
    - 유지/보수 비용 감소
    - 재사용성
    - 확장 가능
    - 캡슐화
    - 독립적
## SFC
- component in Vue
  - Vue에서 component는 이름이 있는 재사용 가능한 Vue instance
  - Vue instance란 new Vue()로 만든 인스턴스
- SFC(Single File Component)
  - 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다
    - 즉, Single File Component
  - Vue instance에서는 HTML, CSS, JS 코드를 한번에 관리
    - 이 Vue instance를 기능 단위로 작성하는 것이 핵심
  - 컴포넌트 기반 개발의 핵심 기능
- 정리
  - HTML, CSS, 그리고 JS를 .vue라는 확장자를 가진 파일 안에서 관리하며 개발
  - 이 파일을 Vue instance, 또는 Vue component라고 하며, 기능 단위로 작성
  - Vue CLI가 Vue를 Component based하게 사용하도록 도와줌
### Vue component
- Vue component 구조
  - 템플릿(HTML)
    - HTML의 body 부분
    - 눈으로 보여지는 요소 작성
    - 다른 컴포넌트를 HTML 요소처럼 추가 가능
    ```vue
    <template>
      <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <HelloWorld msg="Welcome to Your Vue.js App"/>
      </div>
    </template>
    ```
    
  - 스크립트(JS)
    - JS 코드가 작성되는 곳
    - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
    ```vue
    <script>
    import HelloWorld from './components/HelloWorld.vue'
    export default {
      name: 'App',
      components: {
        HelloWorld
      }
    }
    </script>
    ```
  - 스타일(CSS)
    - CSS가 작성되며 컴포넌트의 스타일을 담당
    ```vue
    <style>
    #app {
      font-family: ~~~;
      text-align: ~~;
      color: ~~~;
      margin-top:~~;
    }
    </style>
    ```
- Vue component 구조 정리
  - 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
  - root에 해당하는 최상단의 component가 `App.vue`
  - 이 App.vue를 index.html과 연결
  - 결국 index.html 파일 하나만을 rendering
    - 이게 바로 SPA

### Vue component 실습
- MyComponent.vue
  1. src/components/ 안에 생성
  2. script에 이름 등록
  3. template에 요소 추가
  - 주의) templates 안에는 반드시 하나의 요소만 추가 가능
    - 비어 있어도 안됨
    - 해당 요소 안에 추가 요소를 작성해야 함
- component 등록 3단계
  1. 불러오기
  2. 등록하기
  3. 보여주기
  ```vue
  //App.vue
  <template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기 -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
  </template>
  ```
  ```vue
  <script>
  // 1. 불러오기
  import HelloWorld from './components/HelloWorld.vue'

  export default {
    name: 'App',
    components: {
      // 2. 등록하기
      HelloWorld,
    }
  }
  </script>
  ```
- 자식 컴포넌트 작성 
  - 이제 MyComponent의 자식 컴포넌트를 만들어보자
  - 자식 관계를 표현하기 위해 기존 MyComponent에 간단한 border를 추가
  ```vue
  // MyComponent.vue
  <template>
    <div class="border">
    <h1>This is my component</h1>
    </div>
  </template>
  ```
  ```vue
  <style>
    .border {
      border: solid;
    }
  </style>
  ```
  - src/components/ 안에 MyChild.vue 생성
  ```vue
  // MyChild.vue
  <template>
    <div>
      <h3>This is child component</h3>
    </div>
  </template>
  ```
  ```vue
  <script>
  export default {
    name: 'MyChild'
  }
  </script>
  ```
  - MyComponent에 MyChild 등록
  ```vue
  // MyComponent.vue
  <template>
    <div class="border">
    <h1>This is my component</h1>
    <MyChild/>
    </div>
  </template>
  ```
  ```vue
  <script>
  import MyChild from '@/components/MyChild'

  export default {
    name: 'MyComponent',
    components: {
      MyChild,
    }
  }
  </script>
  ```
  - component의 재사용성
  ```vue
  // MyComponent.vue
  <template>
    <div class="border">
    <h1>This is my component</h1>
    <MyChild/>
    <MyChild/>
    <MyChild/>
    </div>
  </template>
  ```
  ```vue
  //App.vue
  <template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent/>
    <MyComponent/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
  </template>
  ```