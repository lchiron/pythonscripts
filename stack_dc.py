"""
逆波兰表达式
"""

from sstack import SStack

print("\n")
st = SStack()
while True:
    input_ = input()
    for i in input_:
        if i.isdigit():
            st.push(int(i))
        elif i == "-":
            num1 = st.pop()
            num2 = st.pop()
            result = num2 - num1
            st.push(result)
        elif i == "+":
            result = st.pop() + st.pop()
            st.push(result)
        elif i == "*":
            result = st.pop() * st.pop()
            st.push(result)
        elif i == "/":
            num1 = st.pop()
            num2 = st.pop()
            result = num2 / num1
            st.push(result)
        elif i == "p":
            print(st.top())
