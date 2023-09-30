from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    # Здесь реализация вашего решения
   

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))


n = int(input())
sp = input().split()
for i in range(n):
    sp[i] = int(sp[i])
count = 0
sp.insert(0, -274)
sp.append(-274)
i = 1
while i < n + 1:
    if ((sp[i] > sp[i-1]) and (sp[i] > sp[i+1])):
        count += 1
    i += 1
print(count)