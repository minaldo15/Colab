## 제어문
    - 순차, 선택, 반복

- 코드 스타일 가이드
    - 들여쓰기(space sensitive)
        - 문장을 구분할 때, 중괄호({,}) 대신 들여쓰기를 사용
        - 들여쓰기를 할 때는 4칸(space 4번) 혹은 1탭을 입력
            **주의 한코드 안에서는 반드시 한 종류의 들여쓰기를 사용**
        
- 조건문
    - 참/거짓을 판단할 수 있는 조건식과 함께 사용
    ```python
    if 조건 == True
            # Run ~~~~
    else:
            # Run ~~~~ 
      ***
    - 조건문 실습 문제
        - 조건문을 통해 변수 num의 값의 홀수/짝수 여부를 출력하시오.
        - 이때 num은 input을 통해 사용자로부터 입력을 받으시오.
        ***python
        num =int(input())
        if num % 2 == 1: #if num % 2: (0 == False, 0이외에 숫자 == True)
            print('홀수') 
        else:
            print('짝수')
            ```
- 복수 조건문
    - 실습 문제
    ```python
    dust = int(input())
    if dust > 150:
        print('매우나쁨')
        if dust > 300:
            print('실외 활동을 자제하세요')
    elif dust > 80:
        print('나쁨')
    elif dust > 30:
        print('보통')
        if dust < 0:
            print('값이 잘못되었습니다')
    else:
        print('좋음')
    print('미세먼지 확인완료') 
    ```
    **조건식을 동시에 검사하는 것이 아니라 순차적으로 비교**

- 중첩 조건문
    - 조건문은 다른 조건문에 중첩되어 사용될 수 있음
    - 들여쓰기 유의

- 조건 표현식
    - (`true`인 경우 값) `if` 조건 `else` (`false`인 경우 값)

- 반복문
    - `while` 문
    - `for` 문
    - `while`(조건) <-> `for`(반복 횟수)
    - 반복제어
        - `break`, `continue`, (`for-else`)

- `while` 문
    - 복합 연산자(In-Place Operator)
        - 연산과 할당을 합쳐놓은 것(+=)

- `for` 문
    - 처음부터 끝까지 모두 순회하므로 종료 조건이 필요 X
    - `Iterable`
        - 순회할 수 있는 자료형(`string, list, dict, tuple, range, set` 등)
        - 순회형 함수(`range, enumerate`)
    - `for`문을 이용한 문자열(`string`) 순회
        ```python
        - chars = input()
        # happy
        for idx in range(len(chars)): # len(chars) = 5
            print(chars[idx])
            ```
    - 딕셔너리 순회
        - 기본적으로 `key`를 순회
        ```python
        grades = {'john': 80, 'eric': 90}
        for student in grades:
            print(student) # print(student, grades[student])
        '''
        john                           john 80
        eric                           eric 90
        '''
        ```
    - `enumerate` 순회
        - 인덱스와 객체를 쌍으로 담은 열거형(`enumerate`) 객체 반환
        - (`index, value`)형태의 `tuple`로 구성된 열거 객체를 반환
    - List Comprehension
        - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
        - [`code` for 변수 in `iterable` if `조건식`]
        ```python 
        cubic_list = [number ** 3 for number in range(1,4)]
        ```
    - Dictionary Comprehension
        ```python 
        {key: value for 변수 in iterable}
        cubic_list = {number: number ** 3 for number in range(1,4)}
        ```

- 반복문 제어
    - `break` : 반복문 종료
    - `continue` : `continue` 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
    - `for-else` : 끝까지 반복문 실행한 이후에 `else` 문 실행
        - `break`를 통해 중간에 종료되는 경우 `else` 문은 실행되지 않음
    - `pass` : 아무것도 하지 않음(임시용)