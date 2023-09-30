from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    # Здесь реализация вашего решения
    

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))


n = int(input())
m = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(m):
        row[i] = int(row[i])
    a.append(row)
n0 = int(input())
m0 = int(input())
sp_it = []
if n0 > 0:
    n1 = n0 - 1
    m1 = m0
    sp_it.append(a[n1][m1])
if m0 < m - 1:
    n1 = n0
    m1 = m0 + 1
    sp_it.append(a[n1][m1])
if n0 < n - 1:
    n1 = n0 + 1
    m1 = m0
    sp_it.append(a[n1][m1])
if m0 > 0:
    n1 = n0
    m1 = m0 - 1
    sp_it.append(a[n1][m1])
sp_it.sort()
for k in sp_it:
    print(k, end=' ')