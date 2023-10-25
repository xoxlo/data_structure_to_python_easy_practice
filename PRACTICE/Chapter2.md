# 식별자
- 어떤 대상을 유일하게 구별할 수 있는 이름

# 예약어(키워드)
- 이미 특별한 의미가 주어진 이름

# 리터럴(literral) and 자료형(data type)
- 리터럴 : 그 자체가 값을 나타내는 것
- 자료형 : 리터럴들은 그 형태에 따라 자료형이 결정

## 수치
- 내장 자료형 : int(8진수, 16진수 포함), float, complex, bool

## 시퀀스
- 내장 자료형 : str, list, tuple

## 매핑
- dict : 키와 값으로 이루어짐.

## 집합
- set, frozenset

# 변수
- 다른 객체를 참조하는 참조자 또는 포인터의 역할
- 어떠한 변수가 어떠한 리터럴을 참조한다.
    - 쉽게 말해 ' 변수 -> 리터럴 ' 가리킨다.

# 연산자
- 산술, 이항, 증감, 관계, 불리언(boolean)

# 리스트
- 시퀀스형 자료구조
- 리스트를 배열처럼 사용 가능

# 튜플
- 리스트와 유사하지만 크기나 값을 변경할 수 없음
- 튜플만을 이해 추가된 메소드는 X
- 메모리 효율적, 많은 연산 가능

# 딕셔너리
- 키(keys)와 값(values)로 이루어진 항목들의 집합
- 맵(map) 지원

# 집합
- 중복 허용하지 않고, 사이에 순서가 없음
- 선형 자료구조로 보기 어려움

## return
- 여러 개의 결과 반환 가능

## 디폴트 인수(default argument)
- 기본 값을 부여, 기본 값 사용(인수가 생략시), 인수가 주어지면 그 인수 사용

## 키워드 인수(keyword argument)
- end를 지정하지 않으면 기본 값 출력

# 변수의 범위
- 내장 범위, 지역 범위, 전역 범위, 인스턴스 범위

# 모듈과 이름 공간
- 함수나 변수 또는 클래스를 모아 놓은 파일
- 이름공간을 갖고 있음
- 식별자 자유롭게 사용 가능

# 클래스
- 순서지향, 객체지향 기법 모두 지원
- (객체지향) 클래스와 객체가 중심이 되는 기법
- 클래스 -> 틀, 객체 -> 자료 저장

# 생성자
- 자동으로 호출되는 함수
- 데이터 정의 및 초기화
- __init()__로 정해져있음

# 멤버함수
- Method라고 하며, 해당 클래스의 object에서만 호출 가능

# 연산자 중복
- 사용자 정의 클래스 객체들에게 표준 연산자들을 적용할 수 있도록 연산자 중복 허용

# 상속. 부모클래스를 super()로 호출 가능
- 부모클래스는 자식클래스의 부분집합
- 자식클래스에서 부모클래스 멤버함수를 재정의(overriding) 가능
- 자식클래스에서 새롱누 메소드 정의 가능
-----------------------------------------------------