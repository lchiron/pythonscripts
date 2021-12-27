class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class LinkList:
    def __init__(self):
        self.head = Node(None)
        
    def init_list(self, list_):
        p = self.head
        for item in list_:
            p.next = Node(item)
            p = p.next
            
    def show(self):
        p = self.head.next #第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next
            
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False
        
    def clear(self):
        self.head.next = None
        
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)
        
    def head_insert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        
    def insert(self, index, val):
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next 
        p.next = node
        
    def delete(self, x):
        p = self.head
        while p.next and p.next.val !=x:
            p = p.next
            
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next
            
    def get_index(self, index):
        if index < 0:
            raise IndexError("index out of range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range")
            p = p.next
        return p.val
       
        
def merge(l1, l2):
    #将l2合并到l1中
    p = l1.head
    q = l2.head.next
    
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            q = tmp
            p = p.next
    p.next = q
                
        
l1 = [1,2,5,7,9]
l2 = [3,4,8,10]

ll1 = LinkList()
ll2 = LinkList()

ll1.init_list(l1)
# ll1.show()
ll2.init_list(l2)
# ll2.show()


merge(ll1, ll2)

ll1.show()


