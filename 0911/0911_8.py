# for 반복문

print('1부터 n까지 정수 합 구하기')
n = int(input('정수 n 입력: '))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'1부터 {n}까지 정수 합은 {sum}이다.')
