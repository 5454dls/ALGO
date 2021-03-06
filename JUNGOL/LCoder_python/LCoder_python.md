# 1. 목적

- 문법 복습
- 익숙하게 코딩
- 기본기 다지기



# 2. 계획

- 06.03: 출력, 변수와 입력
- 06.04: 연산자, 문자열1
- 06.07: 리스트1, 선택제어문
- 06.08: 디버깅, 반복제어문1
- 06.09: 반복제어문2, 반복제어문3
- 06.10: 문자열2, 리스트2
- 06.11: 리스트3, 기타 자료형
- 06.12: 함수1, 함수2
- 06.13: 함수3, 클래스
- 06.14: 파일입출력



# 3. 피드백

- 06.03(700 ~ 732)
  - 문제를 잘 읽자
  - `input()`에는 띄어쓰기가 디폴트가 아니다.
  - `print()`에는 `,`에 의해 띄어쓰기가 디폴드로 되어 있다.
  - f-string에서 소숫점 표기 `{변수:.원하는 자릿수f}`
- 06.04(740 ~ 769)
  - print : `sep` = `,`를 썼을 때 구분 / `end` = `print`문이 끝난 후 구분
  - 공백제거 : `.strip()` = 양쪽 공백 제거 / `.rstrip()` = 오른쪽 공백 제거 / `.lstrip()` = 왼쪽 공백 제거
  - 줄맞춤 : `.ljust()` = 왼쪽 줄맞춤 / `.center()` = 가운데 줄맞춤 / `.rjust` = 오른쪽 줄맞춤
    - 인자1 : 자리수
    - 인자2 : 공백 채움(option)
- 06.10(781 ~ 814)
  - 공백 없는 문자열을 하나씩 list에 넣기 : `list(str)`
  - 공백 있는 문자열을 하나씩 list에 넣기 : `str.split()`
  - list를 역순으로 출력하기 : `reversed(list)`, `list.reverse()`, `list[::-1]`
  - [e, e, e, ...] : `[element] * num`
- 06.21(817 ~ 831)
  - Vscode를 활용한 디버그
    - Run > start Debugging
    - break point 설정 > 재생 버튼
    - break point에서 계산된 변수 값 등을 확인해볼 수 있다.
    - 이외에 직접 윗버튼과 아래버튼을 클릭하여 확인하는 것도 가능하다. 

- 06.23(841 ~ 859)
  - `round(float, index)` vs `.(index)f`
    - 같은 기능을 수행
    - 전자는 0이 있을 경우 생략, 후자는 0을 표기

- 06.28(861 ~ 878)
  - 아스키코드 변환
    - 숫자 > 문자 : `chr()`
    - 문자 > 숫자 : `ord()`

* 06.29(880 ~ 893)
  * `'구분자'.join(literable)`
  * 문자열 확인
    * 숫자 : `isdigit()`
    * 대문자 : `isupper()`
    * 소문자 : `islower()`
  
* 0630(901 ~ 919)
  * sort 기능
    * `reversed(l)` : 복사 후 정렬 > 정렬된 객체 반환
    * `l.reverse()` : 원본 정렬 > None 반환
    * `l.sort(reverse, key)` : `reverse()`와 같은 기능을 하지만, 오름차순/내림차순,  정렬기준 설정 등의 기능이 있음
  
* 0701(921 ~ 940)

* 0705(941 ~ 953)
  * set 관련 메서드
    * `|` : 합집합
    * `&` : 교집합
    * `-` : 차집합
  * dict 관련 메서드
    * `in` : 기본적으로 key로 순회
    * `items()` : key, value
    * `keys()` : key
    * `values()` : value
    * `get(key, default)` : 특정 key에 맞는 value, 없을 시 default를 반환
  
* 0706(961 ~ 973)

* 0707(981 ~ 992)

  * 버블 정렬

    * ```python
      def bubble(l):
          for i in range(len(l) - 1):
              for j in range(len(l) - i - 1):
                  if l[j] > l[j + 1]:
                      l[j], l[j + 1] = l[j + 1], l[j]
              for n in l:
                  print(n, end = " ")
              print()
      
      l = list(map(int, input().split()))
      bubble(l)
      ```

- 0708(401 ~ 412)

  - n 개중 k를 고르는 조합, 중복조합, 순열, 중복순열

  - 조합

    - ```python
      def com(level, s):
          if level == k:
              print(l)
          else:
              for i in range(s, n - (k + level) + 1):
                  l[level] = arr[i]
                  com(level + 1, i + 1)
      ```

  - 중복조합

    - ```python
      def Hcom(level, s):
          if level == k:
              print(l)
          else:
              for i in range(s, n):
                  l[level] = arr[i]
                  com(level + 1, i)
      ```

  - 순열

    - ```python
      def per(level):
          if level == k:
              print(l)
          else:
              for i in range(n):
                  if not visited[i]:
                  	l[level] = arr[i]
                  	visited[i] = 1
                      per(level + 1)
                      visited[i] = 0
      ```

  - 중복순열

    - ```python
      def per(level):
          if level == k:
              print(l)
          else:
              for i in range(n):
                  l[level] = arr[i]
                  per(level + 1)
      ```

- 0711(421 ~ 431)

- 0718(441 ~ 456)
