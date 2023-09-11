# 조건문과 분기
# 입력 받은 정수의 부호(양수,음수,0) 출력

n = int(input('정수 입력: '))

if n > 0:                  # 1
    print('이 수는 양수')
elif n < 0:                # 2
    print('이 수는 음수')
else:                      # 3
    print('0')

# 실행되는 부분은 1, 2, 3 중 한 곳이며,
# 2개가 동시에 실행되거나, 하나도 실행되지 않는 경우는 없음
# 이 프로그램은 세 개로 분기하기 때문
