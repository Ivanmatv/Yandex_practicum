class Stack:    
    def __init__(self):
            self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
line = list(input())
d = {'(':')','{':'}','[':']'}
s = Stack()
for x in line:
    if x in d.keys():
        s.push(x)
    elif not s.isEmpty() and d[s.peek()] == x:
        s.pop()
    else:
        s.push(x)
        break
if s.isEmpty():    
    print('True')
else:
    print('False')