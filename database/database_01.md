# Database
- INDEX
  1. 데이터의 시대
  2. 데이터베이스
  3. 관계형 데이터베이스
  4. DBMS
  5. SQL

## 데이터베이스
- 데이터베이스의 종류
  - SQL(관계형 데이터베이스) vs NoSQL(비관계형 데이터베이스)
  - 관계형 데이터베이스
    - 표 형식으로된 데이터베이스
    - SQLite, MySQL, ORACLE, etc
  - 비관계형 데이터베이스
    - 관계형 데이터베이스 한계를 극복하기 위해 조금 더 유연한 데이터베이스
    - 메인은 관계형데이터베이스, 비관계형은 서브 데이터베이스로 두고 빠른 처리 확장이 필요한 기능에서 사용

## 관계형 데이터베이스
- 관계형 데이터베이스(RDB)
  - 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
  - 구조화해서 저장하므로 보다 체계적으로 데이터를 저장하고 관리할 수 있음
  - 자료를 여러 테이블로 나누어서 관리하고, 테이블간 관계를 설정해 여러 데이터를 조작할 수 있음
  - 데이터의 무결성(`정확성, 일관성`) 유지에 장점이 있음
  - SQL을 사용하여 데이터를 조회하고 조작

- 관게형 데이터 베이스의 구조
   1. 스키마
   2. 테이블
       - 필드
       - 레코드
       - 기본 키

- 스키마
  - 테이블의 구조
  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술 한 것

- 테이블
  - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
  - 관계(relation)라고도 부름
  1. 필드
      - 속성, 컬럼
  2. 레코드
      - 튜플, 행

- PK(Primary Key)
  - 기본 키
  - 각 레코드의 고유한 값
    - 각각의 데이터를 구분할 수 있는 고윳값
  - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값
  - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용

- FK(Foreign Key)
  - 외래 키
  - 한 테이블의 속성 중 `다른 테이블`의 레코드를 식별할 수 있는 키
  - 다른 테이블의 `기본 키`를 참조
  - 참조하는 테이블의 속성 1개의 값은, 참조되는 측 테이블의 레코드 값에 대응됨
  - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음

## SQL
- Structured Query Language
  - 관계형 데이터베이스에서 데이터를 관리하기 위해 사용하는 언어
  - `데이터베이스 관리 + CRUD 하는 언어`

## SQL Commands
- SQL Commands 종류
  1. DDL(Data Definition Language)
     - 관계형 데이터베이스 구조(테이블, 스키마)를 정의(생성, 수정 및 삭제)하기 위한 명령어
     - CREATE, DROP, ALTER
  2. DML(Manipulation)
     - 데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어
     - INSERT, SELECT, UPDATE, DELETE
  3. DCL(Control)

## SQL Syntax
- SQL Syntax
  - 모든 SQL 문(statement)은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고, 하나의 statement는 세미콜론(;)으로 끝남
    - 세미콜론은 각 SQL 문을 구분하는 표준 방법
  - SQL 키워드는 대소문자를 구분하지 않음
    - 즉, SELECT와 select는 SQL 문에서 동일한 의미
    - 하지만 대문자로 작성하는 것을 권장
  - SQL에 대한 세부적인 문법 사항들은 이어지는 DDL, DML을 진행하며 익혀볼 것
- [참고] Statement & Clause
  - Statement(문)
    - 독립적으로 실행할 수 있는 완전한 코드 조각
    - statement는 clause로 구성됨
  - Clause(절)
    - statement의 하위 단위
```SQL
SELECT column_name FROM table_name
```
- SELECT statement라 부름
- 이 statement는 다음과 같이 2개의 clause로 구성 됨
  1. SELECT column_name
  2. FROM table_name

# DDL
- DDL INDEX
  - CREATE TABLE
  - SQLite Data Types
  - Constraints
  - ALTER TABLE
  - DROP TABLE
## CREATE TABLE
- CREATE TABLE statement
  - 데이터베이스에 새 테이블을 만듦
- CREATE TABLE 실습
  - contacts 테이블 생성
  ```SQL
  CREATE TABLE contacts(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE,
  );
  ```
  - Query 실행하기
    - 실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼
      - 'Run Selected Query '선택
    - 명령문을 모두 선택 할 필요 없으며, 실행하고자 하는 명령문 안에 커서가 올라가 있으면 가능
  - 쿼리 실행 후 테이블 및 스키마 확인
  - 먼저 테이블을 생성하면서 작성한 "데이터 타입"과 "제약조건"을 알아본다.

## SQLite Data Types
- Data Types 종류
  1. NULL
   - NULL value
   - 정보가 없거나 알 수 없음을 의미

  2. INTEGER
   - 정수
   - 크기에 따라 0,1,2,3,4,6 또는 8바이트와 같은 가변 크기를 가짐

  3. REAL
   - 실수
   - 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
  
  4. TEXT
   - 문자 데이터
  
  5. BLOB(Binary Large Object)
   - 입력된 그대로 저장된 데이터 덩어리(대용 타입 없음)
   - 바이너리 등 멀티미디어 파일
   - 예시
     - 이미지 데이터

- Type Affinity
  - "타입 선호도"
  - 특정 컬럼에 저장된 데이터에 권장되는 타입
  - 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
     1. INTEGER
     2. TEXT
     3. BLOB
     4. REAL
     5. NUMERIC
  - 타입 선호도 존재 이유
    -  다른 데이터베이스 엔진 간의 `호환성`을 최대화
    -  정적이고 엄격한 타입을 사용하는 데이터베이스 SQL문을 SQLite에서도 작동하도록 하기 위함

## Constraints
- 개요
  - "제약조건"
  - 입력하는 자료에 대해 제약을 정함
  - 제약에 맞지 않다면 입력이 거부됨
  - 사용자가 원하는 조건의 데이터만 유지하기 위한 즉, `데이터의 무결성`을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약
- 데이터 무결성
  - 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
    - 무결성이란 데이터의 정확성, 일관성을 나타냄
  - 데이터베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적

- Constraints 종류
  1. NOT NULL
      - 컬럼이 NULL 값을 허용하지 않도록 지정
      - 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함
  2. UNIQUE
      - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
  3. PRIMARY KEY
      - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
      - 각 테이블에는 하나의 기본 키만 있음
      - 암시적으로 NOT NULL 제약 조건이 포함되어 있음
  4. AUTOINCREMENT
      - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
      - INTEGER PRIMARY KEY 다음에 작성하면 해당 `rowid`를 다시 재사용하지 못하도록 함
      - Django에서 테이블 생성 시 id 컬럼에 기본적으로 사용하는 제약조건
  5. 기타 Constraints

- rowid의 특징
  - 테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성됨
  - 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값
  - 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
    - 값은 1에서 시작
    - 데이터 삽입 시에 rowid 또는 INTEGER PRIMARY KEY 컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당
  
  - 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)이 됨
    - 즉, 새 컬럼 이름으로 rowid에 액세스 할 수 있으며 rowid 이름으로도 여전히 액세스 가능
  - 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않는 정수를 찾아 사용
  - 만약 SQLite가 사용되지 않은 정수를 찾을 수 없으면 SQLITE_FULL 에러가 발생
    - 또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서 rowid 값을 재사용하려고 시도

## ALTER TABLE
- 개요
  - "Modify the structure of an existing table."
  - 기존 테이블의 구조를 수정(변경)
  - SQLite의 ALTER TABLE 문을 사용하면 기존 테이블을 다음과 같이 변경할 수 있음
    1. Rename a table
    2. Rename a column
    3. Add a new column to a table
    4. Delete a column
- ALTER TABLE statement
  1. ALTER TABLE RENAME
   ```SQL
   ALTER TABLE contacts RENAME TO new_contacts;
   ```
  2. ALTER TABLE RENAME COLUMN
   ```sql
   ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
   ```
  3. ALTER TABLE ADD COLUMN
   ```SQL
   ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
   ```
   - 만약 테이블에 기존 데이터가 있을 경우 다음과 같은 에러가 발생
     - `Cannot add NOT NULL column with default value NULL`
   - 이전에 이미 저장된 데이터들은 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL이 작성됨
   - 그런데 새로 추가되는 컬럼에 NOT NULL 제약조건이 있기 때문에 기본 값 없이는 추가될 수 없다는 에러가 발생한 것
   - 다음과 같이 `DEFAULT` 제약 조건을 사용하여 해결할 수 있음
    ```SQL
   ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';
   ```
   - 이렇게 하면 address 컬럼이 추가되면서 기존에 있던 데이터들의 address 컬럼 값은 'no address'가 됨

  4. ALTER TABLE RENAME DROP COLUMN
   ```SQL
   ALTER TABLE new_contacts DROP COLUMN address;
   ```
   - 단 삭제하지 못하는 경우가 있음
     - 컬럼이 다른 부분에서 참조되는 경우
       - FOREIGN KEY 제약조건에서 사용되는 경우
     - PRIMARY KEY인 경우
     - UNIQUE 제약 조건이 있는 경우

## DROP TABLE
- DROP TABLE 특징
  - 한 번에 하나의 테이블만 삭제할 수 있음
  - 여러 테이블을 제거하려면 여러 DROP TABLE 문을 실행해야 함
  - DROP TABLE 문은 실행 취소하거나 복구할 수 없음
    - 따라서 각별히 주의하여 수행해야 한다.

# DML
- DML INDEX
  - Simple query
  - Sorting rows
  - Filtering data
  - Grouping data
  - Changing data

- sqlite3 사용하기
  - 시작하기 -> sqlite3
  - 데이터베이스 파일 열기 -> .open mydb.sqlite3 / sqlite3 mydb.sqlite3
  - 종료하기 -> .exit
- CSV 파일을 SQLite 테이블로 가져오기
  - sqlite3 tool을 사용하여 CSV 파일을 테이블로 가져오는 방법
  1. DML.sql 파일 생성
  2. 테이블 생성하기 -> CREATE TABLE users(~,~,~);
  3. 데이터베이스 파일 열기 -> sqlite3 mydb.sqlite3
  4. 모드(.mode)를 csv로 설정 -> .mode csv
  5. .import 명령어를 사용하여 csv 데이터를 테이블로 가져오기 -> .import users.csv users
  6. import 된 데이터 확인하기
   - sqlite3 tool 에서도 SQL 문을 사용할 수 있지만, 실습의 편의와 명령어 기록을 위해 sql 확장자 파일에서 진행하도록 함

## Simple query
- 개요
  - select문을 사용하여 간단하게 단일 테이블에서 데이터를 조회하기
- SELECT statement
  ```sql
  SELECT column1, column2 FROM table_name;
  ```
  - 특정 테이블에서 데이터를 조회하기 위해 사용
  - 문법 규칙
    1. SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
    2. FROM 절(clause)에서 데이터를 가져올 테이블을 지정
  - SELECT 문은 SQLite에서 가장 복잡한 문
  - 다양한 절과 함께 사용할 수 있음
    - ORDER BY
    - DISTINCT
    - WHERE
    - LIMIT
    - LIKE
    - GROUP BY
 
- SELECT statement 실습
  - SELECT * FROM 테이블명
    - '테이블명'에 있는 모든 컬럼 조회 == 모든 데이터 조회
  - 이름과 나이 조회하기
    ```sql
    SELECT first_name, age FROM users;
    ```
  - rowid 와 이름 조회하기
    ```sql
    SELECT rowid, first_name FROM users;
    ```

## SOrting rows
- 개요
  - ORDER BY 절을 사용하여 쿼리의 결과를 정렬하기
- ORDER BY clause
    ```sql
    SELECT select_list FROM table_name
    ORDER BY column_1 ASC, column_2 DESC;
    ```
  - SELECT 문에 추가하여 결과를 정렬
  - ORDER BY 절은 FROM 절 뒤에 위치함
  - 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있음
  - 이를 위해 ORDER BY 절 다음에 'ASC'(오름차순) 또는 'DESC'(내림차순) 키워드를 사용
- ORDER BY clause 실습
  - 이름과 나이를 나이가 어린 순서대로 조회하기
    ```sql
    SELECT first_name, age FROM users
    ORDER BY age ASC;
    ```
    - ASC 생략가능
  - 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기
    ```sql
    SELECT first_name, age, balance FROM users
    ORDER BY age, balance DESC;
    ```
    - ORDER BY절은 하나 이상의 컬럼을 정렬할 경우 첫 번째 열을 사용하여 행을 정렬하고, 그런 다음 두번째 컬럼을 사용하여 정렬되어 있는 행을 정렬하는 방식
    - 즉, 먼저 age를 기준으로 먼저 오름차순으로 정렬하고, 이 결과를 balance를 기준으로 내림차순으로 정렬한 것
    - [참고] NULL 값은 다른 값보다 제일 작은 것으로 간주

## Filtering data
- 개요
  - 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
  - Clause
    - SELECT DISTINCT
    - WHERE
    - LIMIT
  - Operator
    - LIKE
    - IN
    - BETWEEN

- SELECT DISTINCT clause
  ```sql
  SELECT DISTINCT select_list FROM table_name;
  ```
  - 조회 결과에서 중복된 행을 제거
  - DISTINCT 절은 SELECT에서 선택적으로 사용할 수 있는 절
  - 문법 규칙
    1. DISTINCT 절은 SELECT 키워드 바로 뒤에 나타나야 함
    2. DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성
- SELECT DISTINCT 실습
  - 중복없이 모든 지역 조회하기
  ```sql
  SELECT DISTINCT country FROM users;
  ```
  - 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기
  ```sql
  SELECT DISTINCT country FROM users ORDER BY country;
  ```
  - [참고] SQLite는 NULL 값을 중복으로 간주

- WHERE clause
  ```sql
  SELECT column_list FROM table_name
  WHERE search_condition;
  ```
  - 조회 시 특정 검색 조건을 지정
  - WHERE 절은 SELECT 문에서 선택적으로 사용할 수 있는 절
    - SELECT 문 외에도 UPDATE 및 DELETE 문에서 WHERE 절을 사용할 수 있음
  - FROM 절 뒤에 작성
- WHERE clause 검색 조건 작성 형식
  - WHERE left_expression COMPARISON_OPERATOR right_expression
  ```sql
  WHERE column_1 = 10
  WHERE column_2 LIKE 'KO%'
  WHERE column_3 IN (1,2)
  WHERE column_4 BETWEEN 10 AND 20
- WHERE 실습
  - 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
  ```sql
  SELECT first_name, age, balance FROM users
  WHERE age >= 30 AND balance > 500000;
  ```

- LIKE operator
  - 패턴 일치를 기반으로 데이터를 조회
  - SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용
  - 기본적으로 대소문자를 구분하지 않음
    - 'A' LIKE 'a'는 true
  - SQLite는 패턴 구성을 위한 두 개의 와일드카드를 제공
    1. %(percent)
       - 0개 이상의 문자가 올 수 있음을 의미
       - '영%' 패턴은 영으로 시작하는 모든 문자열과 일치(영, 영미, 영미리 등)
       - '%도' 패턴은 도로 끝나는 모든 문자열과 일치(도, 수도, 경기도 등)
    2. _(underscore)
        - 단일(1개) 문자가 있음을 의미
        - '영_' 패턴은 영으로 시작하고 총 2자리인 문자열과 일치(영미, 영수 등)
        - '_도' 패턴은 도로 끝나고 총 2자리인 문자열과 일치(수도, 과도 등)
- LIKE 실습
  - 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
  ```sql
  SELECT first_name, phone FROM users
  WHERE phone LIKE '%-51__-%';
  ```

- IN operator
  - 값이 값 목록 결과에 있는 값과 일치하는지 확인
  - 표현식이 값 목록의 값과 일치하는지 여부에 따라 true 또는 false를 반환
  - IN 연산자의 결과를 부정하려면 NOT IN 연산자를 사용
- IN 실습
  - 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
  ```sql
  SELECT first_name, country FROM users
  WHERE country IN ('경기도', '강원도');
  ```

- BETWEEN operator
  - 값이 값 범위에 있는지 테스트
  - 값이 지정된 범위에 있으면 true를 반환
  - SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용
  - BETWEEN 연산자의 결과를 부정하려면 NOT BETWEEN 연산자를 사용
- BETWEEN 실습
  - 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
  ```sql
  SELECT first_name, age FROM users
  WHERE age BETWEEN 20 AND 30;
  ```

- LIMIT clause
  ```sql
  SELECT column_list FROM table_name LIMIT row_count;
  ```
  - 쿼리에서 반환되는 행 수를 제한
  - SELECT 문에서 선택적으로 사용할 수 있는 절
  - row_count는 반환되는 행 수를 지정하는 양의 정수를 의미

- LIMIT 실습
  - 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
  ```sql
  SELECT first_name, balance FROM users
  ORDER BY balance DESC LIMIT 10;
  ```
  - 나이가 가장 어린 5명의 이름과 나이 조회하기
  ```sql
  SELECT first_name, age FROM users
  ORDER BY age LIMIT 5;

- OFFSET keyword
  - LIMIT 절을 사용하면 첫 번째 데이터부터 지정한 수 만큼의 데이터를 받아올 수 있지만, OFFSET과 함께 사용하면 특정 지정된 위치에서부터 데이터를 조회할 수 있음
  - 11번째부터 20번째 데이터의 rowid와 이름 조회하기
  ```sql
  SELECT rowid, first_name FROM users
  LIMIT 10 OFFSET 10;
  ```