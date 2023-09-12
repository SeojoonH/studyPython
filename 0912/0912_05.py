# *를 n개 출력하되 w개마다 줄바꿈하기 2

print('* 출력')
n = int(input('몇 개 출력: '))
w = int(input('몇 개마다 줄바꿈: '))

for _ in range(n // w):      # n // w번 반복
    print('*' * w)

rest = n % w
if rest:        # if 문 판단 1번
    print('*' * rest)
