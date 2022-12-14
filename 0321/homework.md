## 0321 HW

1. **논리와 증명 12번**

   **n^2이 3의 배수면 n은 3의 배수임을 증명하라**

   ```python
   n^2이 3의 배수이다 -> n^2은 3과 다른 정수의 곱으로 나타낼 수 있다.
   n^2 = 3*a, a는 0이 아닌 정수, 조건에 따라 n^2은 반드시 양수이므로 a는 자연수
   
   # 양변에 루트 씌우기
   n = 3^(0.5)*a^(0.5)
   
   # n이 3의 배수인지 판별하기
   n/3 = 3^(-0.5)*a^(0.5) -> 얘가 정수이면 참. 즉, 3^(-0.5)*a^(0.5) 이 부분이 정수인지 아닌지 판별해야 한다
   
   # 판별하기
   모든 자연수 a에 대하여 n/3 = 3^(-0.5)*a^(0.5)식을 구성하는데에 모순이 없다
   그러므로 3^(-0.5)*a^(0.5)는 정수가 '아닐수도 있다'
   
   -> n^2가 3의 배수라고 해서 반드시 n이 3의 배수가 되는것은 아니다
   
   # 반례
   n = 6^(0.5)
   ```

   

2. **기초 수식 1**

   **T(n) = T(n-1) + 1, T(0) = 1**

   ```python
   T(0) = 1
   T(n) = T(n-1) + 1 = T(n-2) + 1 + 1 = T(n-3) + 1 + 1 + 1
   T(n-1) = T(n-2) + 1 = T(n-3) + 1 + 1
   T(n-2) = T(n-3) + 1
   
   T(n) = T(n-k) + k
   n = k일때
   T(k) = T(0) + k, T(0) = 1이므로 T(k) = k + 1
   
   O(n)
   ```



3. **기초 수식 2**

   **T(n) = T(n-1) + n, T(0) = 1**

   ```python
   T(0) = 1
   T(n) = T(n-1) + n = T(n-2) + n-1 + n = T(n-3) + n-2 + n-1 + n = T(n-3) + 3n - 3 = T(n-4) + 4n - 6
   T(n-1) = T(n-2) + n-1 = T(n-3) + n-2 + n-1 = T(n-3) + 2n - 3 = T(n-4) + 3n - 6
   T(n-2) = T(n-3) + n-2 = T(n-4) + 2n - 5
   T(n-3) = T(n-4) + n-3
   
   T(n) = T(n-k) + 4k + a*n^2
   n = k일때
   T(k) = T(0) + 4k + a, T(k) = 4k + a*k^2 + 1
   
   O(n^2)
   ```

   