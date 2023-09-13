# for 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:

    for i in range(len(a)):
        if a[i] == key:
            return i      # 검색 성공시 인덱스 반환
    return -1             # 검색 실패시 -1 반환


if __name__ == '__main__':
    num = int(input('원소 수 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색 값 입력: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값 갖는 원소 존재하지 않음')
    else:
        print('검색값은 x[{idx}]')
