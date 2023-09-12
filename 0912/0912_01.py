# 반복 과정 조건 판단 2
# + - 번갈아 출력하기 1

print('+ - 번갈아 출력.')
n = int(input('몇 개를 출력: '))

for i in range(n):
    if i % 2:                 # 홀수인 경우 - 출력
        print('-', end='')
    else:
        print('+', end='')    # 짝수인 경우 + 출력

print()

# for 문 반복 n번, 나눗셈 n번, if 문 판단 n번

# 문제점 2가지
# 1. for 문 반복할 때마다 if 문 수행
# 2. 상황에 따라 유연하게 수정하기 어려움
