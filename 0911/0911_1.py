# 세 정수를 입력 받아 최대값 구하기

a = int(input('a 입력: '))
b = int(input('b 입력: '))
c = int(input('c 입력: '))

maximum = a
if b > maximum:
  maximum = b
if c > maximum:
  maximum = c

print(f'최대값은 {maximum}이다.')