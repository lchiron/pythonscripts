
class QueueError(Exception):
    pass

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class LinkQueue:
    # front and tail 侵占一个Node
    # 没有无用节点head
    def __init__(self):
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear

    #入队 rear动
    def inqueue(self, val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    #出队 front动
    def outqueue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front.val


if __name__ == "__main__":
    ls = LinkQueue()
    ls.inqueue(1)
    ls.inqueue(2)
    ls.inqueue(3)
    print(ls.outqueue())