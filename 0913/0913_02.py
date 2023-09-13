# 10진수 정수 입력 받아 2~36진수로 변환해 출력하기

def card_conv(x: int, r: int) -> str:

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]


if __name__ == '__main__':
    print('10진수를 n진수로 변환')

    while True:
        while True:
            no = int(input('변환할 값 양의 정수 입력: '))
            if no > 0:
                break

        while True:
            cd = int(input('원하는 변환 진수 입력: '))
            if 2 <= cd <= 36:
                break

        print(f'{cd} 진수로는 {card_conv(no, cd)}이다.')

        retry = input('한 번 더 변환? (Y / N): ')
        if retry in {'N', 'n'}:
            break
