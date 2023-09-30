from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    zippy = []
    for i in range(len(a)):
        zippy.append(f'{a[i]} {b[i]}')
    return zippy

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
