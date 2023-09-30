def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    n = int(input())
    sp = input().split()
    long_word = sp[0]
    i = 1
    while i < len(sp):
        if (len(sp[i]) > len(long_word)):
            long_word = sp[i]
        i += 1
    return long_word
    return len(long_word)

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))


n = int(input())
sp = input().split()
long_word = sp[0]
i = 1
while i < len(sp):
    if (len(sp[i]) > len(long_word)):
        long_word = sp[i]
    i += 1
print(long_word)
print(len(long_word))