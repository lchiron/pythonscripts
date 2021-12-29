
class StackError(Exception):
    pass

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Linkstack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, val):
        # node = Node(val)
        # node.next = self._top
        # self._top = node
        self._top = Node(val, self._top)

    def pop(self, val):
        if self._top is None:
            raise StackError("Stack is empty")
        value = self._top.val
        self._top = self._top.next
        return value

    def top(self):
        if self._top is None:
            raise StackError("Stack is empty")
        return self._top.val

if __name__ == "__main__":
    ls = Linkstack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls.top())