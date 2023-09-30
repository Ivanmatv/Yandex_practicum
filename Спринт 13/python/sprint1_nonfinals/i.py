def is_power_of_four(number: int) -> bool:
    # Здесь реализация вашего решения
    pass

print(is_power_of_four(int(input())))


chislo = int(input())
while True:
    if chislo == 1:
        flag = True
        break
    chislo = chislo / 4
    if (chislo % 4 > 0 and chislo != 1):
        flag = False
        break
print(flag)