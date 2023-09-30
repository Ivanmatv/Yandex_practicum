# ID 82756473

"""Быстра сотрировка.
Быстрая сортировка – разделяет коллекцию на две (примерно) равные части,
принимая псевдослучайный элемент и используя его в качестве опоры (как бы
центра деления). Элементы, меньшие, чем опора, перемещаются влево от опоры,
а элементы, размер которых больше, чем опора, справа от него. Этот процесс
повторяется для коллекции слева от опоры, а также для массива элементов справа
от опоры, пока весь массив не будет отсортирован. Эта реализация сортировки
не может потреблять O(n) дополнительной памяти для промежуточных данных (такая
модификация быстрой сортировки называется "in-place").

In-place sort.
Пусть мы как-то выбрали опорный элемент (рандомно!). Заведём два указателя left
и right, которые изначально будут указывать на левый и правый концы отрезка
соответственно. Затем будем двигать левый указатель вправо до тех пор, пока он
указывает на элемент, меньший опорного. Аналогично двигаем правый указатель влево,
пока он стоит на элементе, превосходящем опорный. В итоге окажется, что левее от
left все элементы точно принадлежат первой группе, а правее от right — второй.
Элементы, на которых стоят указатели, нарушают порядок. Поменяем их местами и
продвинем указатели на следующие элементы. Будем повторять это действие до тех
пор, пока left и right не столкнутся.
"""
from dataclasses import dataclass


@dataclass
class Trainee:
    __slots__ = ['username', 'solved', 'penalty']
    username: str
    solved: int
    penalty: int

    def __gt__(self, other: list) -> bool:
        return (
            (-self.solved, self.penalty, self.username) >
            (-other.solved, other.penalty, other.username)
        )

    def __lt__(self, other: list) -> bool:
        return (
            (-self.solved, self.penalty, self.username) <
            (-other.solved, other.penalty, other.username)
        )

    def __str__(self):
        return self.username


def partition(competitors: list, left: int, right: int) -> int:
    """Разделение массива участников на части."""
    pivot = competitors[left]
    i, j = left + 1, right - 1
    while True:
        while i <= j and competitors[j] > pivot:
            j -= 1
        while i <= j and competitors[i] < pivot:
            i += 1
        if i <= j:
            competitors[i], competitors[j] = competitors[j], competitors[i]
        else:
            competitors[left], competitors[j] = competitors[j], competitors[left]
            return j


def quick_sort(competitors: list, left: int, right: int) -> list:
    """Рекурсивный вызвов алгоритма."""
    if right - left > 1:
        p = partition(competitors, left, right)
        quick_sort(competitors, left, p)
        quick_sort(competitors, p + 1, right)


if __name__ == '__main__':
    number = int(input())
    competitors = []
    for _ in range(number):
        username, solved, penalty = input().split()
        competitors.append(Trainee(username, int(solved), int(penalty)))
    left = 0
    quick_sort(competitors, left, number)
    print(*competitors, sep="\n")
