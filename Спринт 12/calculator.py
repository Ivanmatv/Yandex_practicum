# ID 81892870


class Stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()


calculations = {
    '+': lambda a, b: b + a,
    '-': lambda a, b: b - a,
    '*': lambda a, b: b * a,
    '/': lambda a, b: b // a,
}


def calculator_rpn(expression):
    stack = Stack()
    for val in expression.split():
        if val in calculations.keys():
            op1, op2 = stack.pop(), stack.pop()
            stack.push(calculations[val](op1, op2))
        else:
            stack.push(int(val))
    return stack.pop()


if __name__ == '__main__':
    expression = input()
    print(calculator_rpn(expression))