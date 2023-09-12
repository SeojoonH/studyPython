# 오른쪽 아래 직각 이등변 삼각형 * 출력

print('오른쪽 이등변 삼각형 출력')
n = int(input('짧은 변 길이 입력: '))

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')     # 공백을 출력
    for _ in range(i + 1):
        print('*', end='')
    print()
