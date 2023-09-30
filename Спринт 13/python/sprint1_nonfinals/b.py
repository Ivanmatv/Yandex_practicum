def check_parity(a: int, b: int, c: int) -> bool:
    # Здесь реализация вашего решения
    list = [a, b, c]
    i = 0
    while i < len(list):
        for num in list:
            if num % 2 == 0 or num % 2 == 1:
                return True
            else:
                return False

def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))


a, b, c = map(int, input().split())
if (((a%2==1) and (b%2==1) and (c%2==1)) or ((a%2==0) and (b%2==0) and (c%2==0))):
    print('WIN')
else:
    print('FAIL')