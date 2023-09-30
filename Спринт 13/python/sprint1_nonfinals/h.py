from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    # Здесь реализация вашего решения
    pass

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))


ch1 = input()
ch2 = input()
if (len(ch1) >= len(ch2)):
    n = len(ch1)
    ch2 = ch2.zfill(n)
else:
    n = len(ch2)
    ch1 = ch1.zfill(n)
ch1 = list(ch1)
ch2 = list(ch2)
for i in range(len(ch1)):
    ch1[i] = int(ch1[i])
for i in range(len(ch2)):
    ch2[i] = int(ch2[i])
ch1.reverse()
ch2.reverse()
ch_it = []
if (len(ch1) >= len(ch2)):
    n = len(ch1)
else:
    n = len(ch1)
flag = 0
for i in range(n):
    temp = ch1[i] + ch2[i] + flag
    if temp == 0 :
        ch_it.append(0)
    elif temp == 1:
        ch_it.append(1)
        flag = 0
    elif temp == 2:
        ch_it.append(0)
        flag = 1
    else:
        ch_it.append(1)   # равно 3
        flag = 1
if flag == 1:
    ch_it.append(1)
ch_it.reverse()
#print(ch_it)
for i in range(len(ch_it)):
    print(ch_it[i], end='')