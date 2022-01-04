"""
  栈模型顺序存储
"""


# 自定义异常
class StackError(Exception):
    pass

class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶
        self._elems = []

    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self, val):
        self._elems.append(val)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems[-1]


if __name__ == "__main__":
    st = SStack()
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
