# ID 82443253
"""Сортировка по ключу.
В этой сортировке мы указываем опорную точку -
элемент (число), который мы хотим найти в массиве, потом разделяем массив
на две части, каждую которую сортируем по возрастанию, после этого выполняем
бинарный поиск - это алгоритм поиска определенного элемента в списке.
"""


def broken_search(nums: list, target: int) -> int:
    """Алгоритм сортировки по ключу."""
    left_border = 0
    right_border = len(nums) - 1
    while left_border <= right_border:
        middle = (left_border + right_border) // 2
        if nums[middle] == target:
            return middle
        if nums[left_border] <= nums[middle]:
            if nums[left_border] <= target < nums[middle]:
                right_border = middle - 1
            else:
                left_border = middle + 1
        else:
            if nums[middle] < target <= nums[right_border]:
                left_border = middle + 1
            else:
                right_border = middle - 1
    return -1


if __name__ == '__main__':
    n = int(input())
    target = int(input())
    nums = [int(num) for num in input().split()]
    print(broken_search(nums, target))
