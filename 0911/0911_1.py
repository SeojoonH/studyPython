# 세 정수를 입력 받아 최대값 구하기

a = int(input('a 입력: '))
b = int(input('b 입력: '))
c = int(input('c 입력: '))

maximum = a           # 최대값을 a로 지정
if b > maximum:       # b가 a보다 클 경우 b가 최대값
    maximum = b
if c > maximum:       # c가 b보다 클 경우 c가 최대값
    maximum = c

print(f'최대값은 {maximum}이다.')
