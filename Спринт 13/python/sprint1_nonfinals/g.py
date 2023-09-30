def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    pass

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))


n = int(input())
sp = []
if n < 2:
    sp.append(n)
while True:
    sp.append(n % 2)
    n = n // 2
    if n < 2:
        sp.append(n)
        break
sp.reverse()
for i in range(len(sp)):
    print(sp[i], end='')