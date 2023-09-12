# 1부터 n까지 정수 합 구하기(n값은 양수만 입력 받음)

print('1부터 n까지 정수의 합 구하기')

while True:
    n = int(input('n값을 입력: '))
    if n > 0:
        break    # n이 0보다 커질 때까지 반복

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}이다.')

# True를 사용해 의도적으로 while 문이 무한 반복되도록 만든 것. 무한 루프라고 함.
# break를 이용해 무한 루프에서 탈출
