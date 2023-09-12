# 이등변 삼각형 * 출력

print('왼쪽 아래 직각 이등변 삼각형 출력')
n = int(input('짧은 변 길이 입력: '))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()
