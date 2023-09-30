"""
Гоша повесил на стену гирлянду в виде бинарного дерева, в узлах которого находятся лампочки.
У каждой лампочки есть своя яркость. Уровень яркости лампочки соответствует числу, расположенному в узле дерева.
Помогите Гоше найти самую яркую лампочку в гирлянде, то есть такую, у которой яркость наибольшая.

Формат ввода
На вход подается корень дерева.

Формат вывода
Функция должна вернуть максимальное значение яркости в узле дерева.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    if root is None:
        return float('-inf')

    st = root.value
    lis = solution(root.left)
    ris = solution(root.right)

    if lis > st:
        st = lis

    if ris > st:
        st = ris
    return st


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == "__main__":
    test()