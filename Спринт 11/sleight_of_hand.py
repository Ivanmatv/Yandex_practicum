# ID 81532121


def read_input():
    n = int(input()) * 2
    matrix = ''.join([input() for _ in range(4)])
    return n, matrix


def calculations(n, matrix):
    numbers = [0] * 10
    scores = 0
    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers[i] = count

    for i, elem in enumerate(numbers):
        if elem == 0:
            continue
        if int(elem) <= n:
            scores += 1
    return scores


if __name__ == '__main__':
    n, matrix = read_input()
    print(calculations(n, matrix))
