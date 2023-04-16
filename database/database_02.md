## Grouping data
- Aggregate function
  - "집계 합수"
  - 값 집합의 최댓값, 최소값, 평균, 합게 및 개수를 계산
  - 값 집합에 대한 계산을 수행하고 단일 값을 반환
    - 여러 행으로부터 하나의 결과 값을 반환하는 함수
  - SELECT 문의 GROUP BY 절과 함께 종종 사용됨
  - 제공하는 함수 목록
    - AVG(), COUNT(), MAX(), MIN(), SUM()
  - AVG(), MAX(), MIN(), SUM()는 숫자를 기준으로 계산이 되어져야 하기 때문에 반드시 컬럼의 데이터 타입이 숫자(`INTEGER`)일 때만 사용 가능
- Aggregate function 예시
  - users 테이블의 전체 행 수 조회하기
  ```sql
  SELECT COUNT(*) FROM users;
  ```
  - 전체 유저의 평균 balance를 조회하기
  ```sql
  SELECT AVG(balance) FROM users;
  ```

- GROUP BY clause
  ```sql
  SELECT column_1, aggregate_function(column_2) FROM table_name
  GROUP BY column_1, column_2;
  ```
  - 특정 그룹으로 묶인 결과를 생성
  - 선택된 컬럼 값을 기준으로 데이터(행)들의 공통 값을 묶어서 결과로 나타냄

- GROUP BY 실습
  - 지역별 평균 balance 조회하기
  ```sql
  SELECT DISTINCT country, AVG(balance) From users
  GROUP BY country;
  ```
  - 잔고 많은순으로 정렬까지
  ```sql
  SELECT DISTINCT country, AVG(balance) From users
  GROUP BY country ORDER BY avg(balance) DESC;
  ```
  - 각 지역별로 몇 명씩 살고 있는지 조회하기
    - country 컬럼으로 그룹화
    ```sql
    SELECT country FROM users GROUP BY country;
    ```
    - 그룹별로 포함되는 데이터의 수를 구함
    ```sql
    SELECT country, COUNT(*) FROM users GROUP BY country;
    ```
    - `각 지역별로 그룹이 나뉘어졌기 때문에 COUNT(*)는 지역별 데이터 개수를 세게 됨`
  - [참고] COUNT 참고사항
    - COUNT(), COUNT(age), COUNT(last_name) 등 어떤 컬럼을 넣어도 결과는 같음
    - 현재 쿼리에서는 그룹화된 country를 기준으로 카운트 하는 것이기 때문에 어떤 컬럼을 카운트해도 전체 개수는 동일하기 때문
  - 각 성씨가 몇 명씩 있는지 조회하기
    ```sql
    SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
    ```
    - AS 키워드를 사용해 컬럼명을 임시로 변경하여 조회할 수 있음(COUNT(*)->number_of_name)
  - 인원이 가장 많은 성씨 순으로 조회하기
    ```sql
    SELECT last_name, COUNT(*) FROM users
    GROUP BY last_name ORDER BY COUNT(*) DESC;
    ```
## Changing data
- 개요
  - 데이터를 삽입, 수정, 삭제하기
    - INSERT
    - UPDATE
    - DELETE

- INSERT statement
  ```sql
  INSERT INTO table_name (column1, column2, ...)
  VALUES (value1, value2, ...);
  ```
  - 새 행을 테이블에 삽입
  - 문법 규칙
    1. 먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름을 지정
    2. 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록을 추가
       - 컬럼 목록은 선택 사항이지만 컬럼 목록을 포함하는 것이 권장됨
    3. VALUES 키워드 뒤에 쉼표로 구분된 값 목록을 추가
       - `만약 컬럼 목록을 생략하는 경우 값 목록의 모든 컬럼에 대한 값을 지정해야 함`
       - 값 목록의 값 개수는 컬럼 목록의 컬럼 개수와 같아야 함  
- INSERT 사용해보기
  - 단일 행 삽입하기
  ```sql
  INSERT INTO classmates (name, age, address)
  VALUES ('홍길동',23,'서울');
  ```
  - 다음과 같이 작성 할 수도 있음
  ```sql
  INSERT INTO classmates
  VALUES ('홍길동',23,'서울');
  ```
  - 여러 행도 가능
  ```sql
  INSERT INTO classmates 
  VALUES 
    ('홍길동1',23,'서울1'),
    ('홍길동2',23,'서울2'),
    ('홍길동3',23,'서울3'),
    ('홍길동4',23,'서울4'),;
  ```
- UPDATE statement
    ```sql
    UPDATE table_name
    SET column1 = new_value1,
    column2 = new_value2
    WHERE
    search_condition;
    ```
  1. UPDATE 절 이후에 업데이트할 테이블을 지정
  2. SET 절에서 테이블의 각 컬럼에 대해 새 값을 설정
  3. WHERE 절의 조건을 사용하여 업데이트할 행을 지정
      - WHERE 절은 선택 사항.
      - 생략시, 모든 행에 있는 데이터를 업데이트
  4. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트 할 행 수를 지정가능

- UPDATE 실습
  - 2번 데이터의 이름을 '김두루미', 주소를 '제주도'로 수정하기
  ```sql
  UPDATE classmates
  SET name='김두루미',
    address='제주도',
  WHERE rowid = 2;
  ```
- DELETE statement
  ```sql
  DELETE FROM table_name
  WHERE search_condition;
  ```
  - 테이블에서 행을 제거
  - 테이블의 한 행, 여러 행 및 모든 행을 삭제가능
  - 문법 규칙
    1. DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름을 지정
    2. WHERE 절에 검색 조건을 추가하여 제거할 행을 식별
        - WHERE 절은 선택 사항이며, 생략하면 테이블의 모든 행을 삭제
    3. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 삭제할 행 수를 지정가능
- DELETE 실습
  - 5번 데이터 삭제하기
  ```sql
  DELETE FROM classmates WHERE rowid = 5;
  ```
  - 삭제된 것 확인하기
  ```sql
  SELECT rowid, * FROM classmates;
  ```
  - 이름에 '영'이 포함되는 데이터 삭제하기
  ```sql
  DELETE FROM classmates WHERE name LIKE '%영%';
  ```

## 정규형
- 데이터베이스 정규형
  - 데이터베이스를 구조화 하는 방법론
  - 데이터의 중복을 최소화하고 일관성과 무결성을 보장하기 위함
  - 데이터의 구조를 더 좋은 구조로 바꾸는 것을 정규화라고 함
  - 관계형 데이터베이스의 경우 6개의 정규형이 있음
  - 제 1정규형, 제 2정규형, 제 3정규형, ...
- 제 1정규형
  - 하나의 속성값이 복수형을 가지면 안됨
  - 하나의 속성에는 값이 하나만 들어가야 함
- 제 2정규형
  - 테이블의 기본키에 종속되지 않는 컬럼은 테이블이 분리 되어야함
  - 테이블과 관련 없는 애들은 따로 분리하라는 것
- 제 3정규형
  - 다른 속성에 의존(종속)하는 속성은 따로 분리할 것

## JOIN
- 테이블 합치기
  - CROSS JOIN
    ```sql
    SELECT * FROM articles, users 
    WHERE articles.userid=users.rowid;
    ```
  - INNER JOIN
    ```sql
    SELECT * FROM articles INNER JOIN users
    ON userid=users.rowid;
    ```
  - LEFT JOIN
    - `왼쪽 테이블`의 데이터를 기준으로 오른쪽 데이터 결합, 없으면 NULL
  - RIGHT JOIN
    - LEFT 반대

