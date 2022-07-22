# 1. 목적

- 문법 복습
- 익숙하게 코딩
- 알고리즘 연습



# 2. 계획

- 07.19: 도형만들기1
- 07.20: 수학1
- 07.21: 도형만들기2
- 07.22: 수학2
- 07.25: 문자열
- 07.26: 여러가지
- 07.27: 자료처리
- 07.28: 재귀



# 3. 피드백

- 07.20(1291, 1303, 1304, 1307, 1314, 1338, 1339, 1341, 1856, 2046)

- 07.21(1692, 1430, 1071, 1402, 2809, 1658, 1002)

  - 약수구하기

    - N = A * B이므로 약수는 짝을 이루어 나온다. 따라서 아래와 같이 시간복잡도를 줄일 수 있다.

      ```python
      n = int(input())
      
      divisorsList = []
      
      for i in range(1, int(n**(1/2)) + 1):
          if (n % i == 0):
              divisorsList.append(i) 
              if ( (i**2) != n) : 
                  divisorsList.append(n // i)
      
      divisorsList.sort()
      
      for r in divisorsList:
          print(r, end = " ")
      ```

    - A, B ,C의 최대공약수를 구할 때, A와 B의 최대공약수가 D라면, C와 D의 최대공약수가 A, B, C의 최대공약수가 된다.

      ```python
      def MIN(n1, n2):
          n = 1
      
          for i in range(int(min(n1, n2)), 1, -1):
              if (n1 % i == 0) and (n2 % i == 0):
                  n = i
                  break
          nd.pop()
          nd.pop()
          nd.append(n)
      
      def MAX(n1, n2):
          N = n1 * n2
      
          for i in range(int(min(n1, n2)), 1, -1):
              if (n1 % i == 0) and (n2 % i == 0):
                  N = (n1 * n2) // i
                  break
          Nd.pop()
          Nd.pop()
          Nd.append(N)
      
      num = int(input())
      data = list(map(int, input().split()))
      data.sort()
      
      nd = data[:]
      Nd = data[:]
      i = num - 1
      while len(nd) >= 2:
          MIN(nd[i], nd[i - 1])
          MAX(Nd[i], Nd[i - 1])
          i -= 1
      
      print(nd[0], Nd[0])
      ```

- 07.22(1523, 1719, 1329, 1641, 1337, 2071, 1707, 1331, 1495, 2074)

  - 함수를 통한 divide and conquer 방식이 복잡한 문제를 푸는데 유용함.
  - 배열을 활용하는 것이 인덱스 제어에 유리함.
