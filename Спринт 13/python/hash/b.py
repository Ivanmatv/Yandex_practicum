"""
Гоша написал программу, которая сравнивает строки исключительно по их хешам. Если хеш равен, то и строки равны.
Тимофей увидел это безобразие и поручил вам сломать программу Гоши, чтобы остальным неповадно было.
В этой задаче вам надо будет лишь найти две различные строки, которые для заданной хеш-функции будут давать одинаковое значение.
Гоша использует следующую хеш-функцию: h(s)=(S1A^n-1 + S2A^n-2 + ... + Sn-1A + Sn)
для a = 1000 и m = 123 987 123.
В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.
"""


import random
import string


base = 1000
tablesize = 123_987_123


def polynomial_hash(str, p, m):
    power_of_p = 1
    hash_val = 0

    for char in str:
        hash_val = ((hash_val + ord(char) * power_of_p) % m)
        power_of_p = (power_of_p * p) % m

    return int(hash_val)


letters = string.ascii_lowercase
str = ''.join(random.choice(letters) for i in range(10))
hash = polynomial_hash(str[::-1], base, tablesize)
map = {}

while True:
    str = ''.join(random.choice(letters) for i in range(20))
    hash = polynomial_hash(str[::-1], base, tablesize)
    if not map.get(hash):
        map[hash] = str
    else:
        print(f"{str} - {hash}")
        break
