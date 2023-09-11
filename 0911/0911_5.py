# 조건문과 분기
# 입력 받은 정수의 부호(양수,음수,0) 출력

n = int(input('정수 입력: '))

if n > 0:
    print('이 수는 양수')
elif n < 0:
    print('이 수는 음수')
else:
    print('0')
