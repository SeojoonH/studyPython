# 정수 합 구하기 2

a = int(input('정수 a 입력: '))
b = int(input('정수 b 입력: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)

# i가 b보다 크거나 같은지 판단하지 않으므로 효율이 더 좋음
# 판단 횟수가 n번에서 0번으로, 반복 횟소도 1번 감소
