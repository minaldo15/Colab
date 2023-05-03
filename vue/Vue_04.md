# Vue_04
- INDEX
  - Vue Data Management
    - Pass Props
    - Emit Events
  - Lifecycle Hooks

## Vue Data Management
### Data in components
- Data in components
  - 동적 웹페이지는 한페이지 내에서 같은 데이터를 공유 해야 함
    - 하지만 페이지들은 component로 구분이 되어있음
  - MyComponent에 정의된 data를 MyChild에서 사용하기 위해서는 MyChild에도 똑같은 data를 정의
    - MyComponent의 data 변경에 MyChild는 영향을 받지 않고 서로다른 data를 갖게 됨(각 component는 독립적)
  - 동일한 data를 서로 다른 component에서 보여주기위해서는 부모-자식 관계만 데이터를 주고 받게 만듦
- pass props & emit event
  - 부모 => 자식으로의 데이터의 흐름
    - pass props 방식
  - 자식 => 부모로의 데이터 흐름
    - emit event
### Pass Props
- Pass Props
  - 요소의 속성을 사용하여 데이터 전달
  - props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
  - 자식 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
  - 정적인 데이터를 전달하는 경우 static props라고 명시하기도 함
  - 요소에 속성을 작성하듯이 사용 가능하여, `prop-data-name="value"`의 형태로 데이터를 전달
    - 이 때 속성의 키 값은 kebab-case를 사용
  ```vue
  <script>
  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    }
  }
  </script>
  ```
  - Prop 명시
  - 데이터를 받는 쪽, 즉 하위 컴포넌트에서도 props에 대해 명시적으로 작성해주서야 함
  - 전달받은 props를 type과 함께 명시
  - 컴포넌트를 문서화할 뿐만 아니라, 잘못된 타입이 전달하는 경우 브라우저의 JS 콘솔에서 사용자에게 경고
- MyComponent to MyChild
  ```vue
  // MyComponent.vue
  <template>
    <div class="border">
      <h1>This is MyComponent</h1>
      <MyChild static-props="component(부모)에서 child로"/>
    </div>
  </template>
  ```
  ```vue
  // MyChild.vue
  <template>
  <div>
    <h3>This is child component</h3>
    <p>{{staticProps}}</p>
  </div>
  </template>
  ```
  ```vue
  <script>
  export default {
    name: 'MyChild',
    props: {
      staticProps: String,
    }
  }
  </script>
  ```

- Pass Props convention
  - 부모에서 넘겨주는 props
    - `kebab-case`
  - 자식에서 받는 props
    - `camelCase`
  - 부모 템플릿(html)에서 kebab-case로 넘긴 변수를 자식의 스크립트(vue)에서 자동으로 camelCase로 변환하여 인식함
- Dynamic props
  - 변수를 props로 전달할 수 있음
  - v-bind directive를 사용해 데이터를 동적으로 바인딩
  - 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨
- Dynamic props 실습
```vue
// Mycomponent.vue
<template>
<div class="border">
  <h1>This is MyComponent</h1>
  <MyChild static-props="component(부모)에서 child로"
  :dynamic-props="dynamicProps"
  />
</div>
</template>

<script>
export default {
  
  data: function () {
    return {
      dynamicProps: "It is a data"
    }
  },
}
</script>
```
```vue
// MyChild.vue
<template>
  <div>
    <h3>This is child component</h3>
    <p>{{staticProps}}</p>
    <p>{{dynamicProps}}</p>
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
}
</script>
```

- 컴포넌트의 data 함수
  - 각 vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)하여 사용해야 함
  ```vue
  data: function () {
    return {
      // components data in here
    }
  }
  ```
- Pass Props
  - :dynamic-props="dynamicProps"는 앞의 key값(dynamic-props)이란 이름으로 뒤의 ""안에 오는 데이터(dynamic-props)를 전달하겠다는 뜻
  - 즉, :my-props="dynamicProps"로 데이터를 넘긴다면, 자식컴포넌트에서 myProps로 데이터를 받아야 함

- 단방향 데이터 흐름
  - 모든 props는 부모에서 자식으로 즉 아래로 단방향 바인딩을 형성
  - 부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 아님
    - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨
  - 목적
    - 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지
  - 하위 컴포넌트에서 prop을 변경하려고 시도해서는 안되며 그렇게 하면 vue는 콘솔에서 경고를 출력함

### Emit Event
- Emit Event
  - 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 발생시킴
  - 이벤트를 발생시키는게 어떻게 데이터를 전달하는 것인가?
    1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
    2. 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음
- $emit
  - $emit 메서드를 통해 부모 컴포넌트에 이벤트를 발생
    - `$emit('event-name')` 형식으로 사용하며 부모 컴포넌트에 event-name이라는 이벤트가 발생했다는 것을 알림
    - 마치 사용자가 마우스를 클릭하면 click 이벤트가 발생하는 것처럼 $emit('event-name')가 실행되면 event-name 이벤트가 발생하는 것
- Emit Event 실습
```vue
// MyChild.vue
<template>
<div>
  ...
  <button @click="childToParent">클릭</button>
</div>
</template>

<script>
export default {
  ...
  methods: {
    childToParent: function () {
      this.$emit('child-to-parent')
    }
  }
}
</script>
```
  1. 자식 컴포넌트에 버튼을 만들고 클릭 이벤트를 추가
  2. $emit을 통해 부모 컴포넌트에게 child-to-parent 이벤트를 트리거
```vue
// MyComponent.vue
<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild
    ... 
    @child-to-parent="parentGetEvent"
    />
  </div>
</template>

<script>
export default {
  ...
  methods: {
    parentGetEvent() {
      console.log('자식 컴포넌트에서 발생한 이벤트')
    },
  }
}
</script>
```
  - emit된 이벤트를 상위(부모) 컴포넌트에서 청취 후 핸들러 함수 실행

- emit with data
  - 이벤트를 발생(emit)시킬 때 인자로 데이터 전달 가능
  ```vue
  // MyChild.vue
  methods: {
    ChildToParent: function(){
      this.$emit('child-to-parent','child data')
    }
  }
  ```
  - 이렇게 전달한 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능
  ```vue
  // MyComponent.vue
  methods: {
    parentGetEvent: function(inputData) {
      console.log('child component로부터 ${inputData}를 받음')
    }
  }
  ```

- Emit Event 흐름 정리
  1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(ChildToParent) 호출
  2. 호출된 함수에서 $emit을 통해 상위 컴포넌트에 이벤트(child-to-parent) 발생
  3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트(child-to-parent)를 청취하여 연결된 핸들러 함수(parentGetEvent) 호출, 함수의 인자로 전달된 데이터(child data)가 포함되어 있음
  4. 호출된 함수에서 console.log(~child data~) 실행
  
- emit with dynamic data
  - pass props와 마찬가지로 동적인 데이터도 전달 가능
  - 자식 컴포넌트에서 입력받은 데이터를 부모 컴포넌트에게 전달하여 출력해보자
  ```vue
  // MyChild.vue
  <template>
    <div>
      ...
      <input type="text" 
      v-model="childInputData" 
      @keyup.enter="childInput">
    </div>
  </template>
  ```
  ```vue
  // MyChild.vue
  <script>
  export default {
   ...,
    data: function () {
      return {
        childInputData: null,
      }
    },
    methods: {

      childInput: function () {
        this.$emit('child-input', this.childInputData)
        this.childInputData = ""
      }
    }
  }
  </script>
  ```
  ```vue
  // MyComponent.vue
  <template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild
    ...
    @child-input="getDynamicData"
    />
  </div>
  </template>
  ```
  ```vue
  <script>
  import MyChild from '@/components/MyChild'

  export default {
    ...
    methods: {

      getDynamicData: function(input) {
        console.log(`child에서 입력한 ${input}을 출력`)
      }
    }
  }
  </script>
  ```
- emit with dynamic data 흐름 정리
  1. 자식 컴포넌트에 있는 keyup.enter 이벤트를 청취하여 연결된 핸들러 함수(ChildInput) 호출
  2. 호출된 함수에서 $emit을 통해 부모 컴포넌트에 이벤트(child-input)를 발생
    - 이벤트에 v-model로 바인딩 된 입력받은 데이터를 전달
  3. 상위 컴포넌트는 자식 컴포넌트의 이벤트(child-input)를 청취하여 연결된 핸들러 함수(getDynamicData) 호출, 함수의 인자로 전달된 데이터(childInputData)가 포함되어 있음
  4. 호출된 함수에서 console.log(~childInputData~) 실행

- 정리 
  - 자식 컴포넌트에서 부모 컴포넌트로 이벤트를 발생시킴
    - 이벤트에 데이터를 담아 전달 가능
  - 부모 컴포넌트에서는 자식 컴포넌트의 이벤트를 청취
    - 전달받은 데이터는 이벤트 핸들러 함수의 인자로 사용

- pass props / emit event 컨벤션
  - HTML 요소에서 사용할 때는 kebab-case
  - JS에서 사용할 때는 camelCase

## Lifecycle Hooks
- Lifecycle Hooks
  - 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
    - Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM를 업데이트하는 경우 등
  - 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
  - 이를 Lifecycle Hooks이라고 함
