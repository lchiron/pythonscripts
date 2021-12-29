from sstack import *

words = "nihao(nizai), [[[[))){wozhelihaihao, ni ne }, [youkongma]"
words1 = "nihao(nizai), {wozhelihaihao, ni ne }, [youkongma]"
words2 = "nihao((nizai), {wozhelihaihao, ni ne }, [youkongma]"
words3 = "nihao(nizai)), {wozhelihaihao, ni ne }, [youkongma]"
words4 = "nihao(nizai)), {wozhelihaihao, ni ne }}, [youkongma]"
words5 = "nihao(nizai))))), {{{{{wozhelihaihao, ni ne }}, [youkongma]]]]"

ss = SStack()
ss2 = SStack()
success = True
count = 0
def reverse(sign):
    if sign == "}":
        return "{"
    elif sign == ")":
        return "("
    elif sign == "]":
        return "["

for item in words3:
    count += 1
    if item in ["{", "(", "["]:
        ss.push(item)
        ss2.push(count)
    elif item in ["}", ")", "]"]:
        if ss.is_empty():
            success = False
            print("localtion {}, {} used is wrong".format(count, item))

        elif ss.top() == reverse(item):
            ss.push(item)
            ss2.push(count)
            ss.pop()
            ss.pop()
            ss2.pop()
            ss2.pop()
        else:
            ss.push(item)
            ss2.push(count)

while not ss.is_empty():
    success = False
    print("localtionn {}, {} used is wrong".format(ss2.pop(), ss.pop()))

if success == True:
    print("no error found")




