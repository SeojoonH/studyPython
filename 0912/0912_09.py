# 1~12까지 6을 건너뛰고 출력

for i in range(1, 13):
    if i == 6:
        continue
    print(i, end=' ')

print()


# 이 프로그램은 비효율적
# 건너뛰는 판단을 하려면 비용이 많이 들기 떄문
