# ID 81760322

class QueueIsFull(Exception):
    """Ошибка при попытке добавить элемент в заполненную очередь."""
    def __str__(self):
        return repr(self)


class QueueIsEmpty(Exception):
    """Ошибка при попытке извлечь элемент из пустой очереди."""
    def __str__(self):
        return repr(self)


class Deque:
    def __init__(self, max_n):
        self.queue = [None] * max_n
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_front(self, value):
        if self.size == self.max_n:
            raise QueueIsFull
        if self.queue[self.head]:
            self.head = (self.head - 1) % self.max_n
        self.queue[self.head] = value
        self.size += 1

    def push_back(self, value):
        if self.size == self.max_n:
            raise QueueIsFull
        if self.queue[self.tail]:
            self.tail = (self.tail + 1) % self.max_n
        self.queue[self.tail] = value
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise QueueIsEmpty
        x = self.queue[self.head]
        self.queue[self.head] = None
        if self.size > 1:
            self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.size == 0:
            raise QueueIsEmpty
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        if self.size > 1:
            self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x


if __name__ == '__main__':
    n = int(input())
    max_n = int(input())
    queue: Deque = Deque(max_n)
    for _ in range(n):
        operation, *parameters = input().split()
        method = getattr(queue, operation)
        try:
            result = method(*parameters)
        except (QueueIsFull, QueueIsEmpty):
            result = 'error'
        if result is not None:
            print(result)
