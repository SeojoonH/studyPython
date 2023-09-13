# 1,000 이하 소수 나열

counter = 0               # 나눗셈 횟수
ptr = 0                   # 이미 찾은 소수 개수
prime = [None] * 500      # 소수 저장 배열

prime[ptr] = 2            # 2는 소수. 초기값으로 지정
ptr += 1

for n in range(3, 1001, 2):   # 홀수 대상으로 설정
    for i in range(1, ptr):   # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0:
            break             # 나눠 떨어지면 소수가 아니기에 종료

    else:
        prime[ptr] = n        # 소수로 배열 등록
        ptr += 1

for i in range(ptr):          # ptr 소수 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')
