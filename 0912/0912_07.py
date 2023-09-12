# 직사각형 너비로 변 길이 구하기

area = int(input('직사각형 너비 입력: '))

for i in range(1, area + 1):     # 1부터 사각형의 너비 계산
    if i * i > area:
        break
    if area % i:
        continue
    print(f'{i} * {area // i}')
