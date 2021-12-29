"""
  栈模型顺序存储
"""
from sstack import *

    
#自定义异常
class QueueError(Exception):
    pass
    

class SQueue:
    def __init__(self):
        self._elems = []
        
    def is_empty(self):
        return self._elems == []
        
    #入队
    def inqueue(self, val):
        self._elems.append(val)
        
    #出队
    def outqueue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        return self._elems.pop(0)
    
        
if __name__ == "__main__":
    sq = SQueue()
    # sq.inqueue(10)
    # sq.inqueue(20)
    # sq.inqueue(30)
    # print(sq._elems)
    # while not sq.is_empty():
    #     print(sq.outqueue())


#队列翻转
    for i in range(10):
        sq.inqueue(i)

    ss = SStack()
    while not sq.is_empty():
        ss.push(sq.outqueue())
    while not ss.is_empty():
        sq.inqueue(ss.pop())


    while not sq.is_empty():
        print(sq.outqueue())


