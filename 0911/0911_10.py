# 반복 과정 조건 판단 1

print('a부터 b까지 정수 합 구하기')
a = int(input('정수 a 입력: '))
b = int(input('정수 b 입력: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b:                       # i가 b보다 작으면 합 구하는 과정 출력
        print(f'{i} + ', end='')
    else:                           # i가 b보다 작지 않으면 최종값 출력 위해 = 을 출력
        print(f'{i} = ', end='')
    sum += i

print(sum)
