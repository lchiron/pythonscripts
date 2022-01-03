'''

        A
    B           C
            D           E
        F       G   I       H

'''

from squeue import *

#二叉树节点
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Bittree:
    def __init__(self, root=Node):
        self.root = root

    #先序遍历
    def preOrder(self, node):
        if node is None:
            return
        print(node.val, end="")
        self.preOrder(node.left)
        self.preOrder(node.right)


    #中序遍历
    def inOrder(self, node):
        if node is None:
            return

        self.inOrder(node.left)
        print(node.val, end="")
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return

        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val, end="")

    #层次遍历
    """
    让初始节点先入队，谁先出队就遍历谁，并且让它的左右节点分别入队，直到队列为空
    """
    def leverOrder(self, node):
        sq = SQueue()
        sq.inqueue(node)
        while not sq.is_empty():
            node = sq.outqueue()
            #打印出队元素
            print(node.val, end="")
            if node.left:
                sq.inqueue(node.left)
            if node.right:
                sq.inqueue(node.right)

if __name__=="__main__":
    #根据后续便利构建二叉树
    b = Node("B")
    f = Node("F")
    g = Node("G")
    i = Node("I")
    h = Node("H")
    d = Node("D", f, g)
    e = Node("E", i, h)
    c = Node("C", d, e)
    a = Node("A", b, c) #树根

    # 将a作为遍历的起始位置
    bt = Bittree(a)
    bt.preOrder(bt.root)
    print()
    bt.inOrder(bt.root)
    print()
    bt.postOrder(bt.root)
    print()
    bt.leverOrder(bt.root)
