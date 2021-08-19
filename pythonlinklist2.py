class ListNode():     # 初始化 构造函数  
    def __init__(self,val):  
        self.value=val  
        self.next=None

def Creatlist(n):  
    if n<=0:  
        return False  
    if n==1:  
        return ListNode(1)    # 只有一个节点  
    else:  
        root=ListNode(1)  
        tmp=root  
        for i in range(2,n+1):       #  一个一个的增加节点  
            tmp.next=ListNode(i)  
            tmp=tmp.next  
    return root            # 返回根节点 

def printlist(head):       # 打印链表 （遍历） 
    p=head  
    while p!=None:  
        print(p.value)  
        p=p.next  

def listlen(head):       # 链表长度  
    c=0  
    p=head  
    while p!=None:  
        c=c+1  
        p=p.next  
    return c  

def afterappend(head, value): # 在list的后面插入元素 
    p = head
    t = ListNode(value)
    if p == None:
        p.next = t
    else:
        while p.next != None:
            p = p.next
        p.next = t
    return p 

def preappend(head,value):  # 在list的前面插入元素 
    p = head
    t = ListNode(value)
    t.next = p
    p = t 
    return head

def insert(head,n,value):         # 在n的后面插入元素  
    if n<1 or n>listlen(head):  
        return  
  
    p=head  
    for i in range(1,n):  # 循环四次到达 5  （只能一个一个节点的移动 range不包含n-1）
        p=p.next   
    t=ListNode(value) 
    t.next=p.next   
    p.next=t   
    return head  

def dellist(head,n):  # 删除链表  
    if n<1 or n>listlen(head):  
        return head  
    elif n == 1:  
        head=head.next   # 删除头  
    else:  
        p=head  
        for i in range(1,n-1):    
            p=p.next     # 循环到达 2次   
        q=p.next  
        p.next=q.next    # 把5放在3的后面  
    return head 

def addTwoNumbers(l1, l2):
    ans = ListNode(0)
    tmp = ans
    tmpsum = 0
    while True:
        #依次遍历l1 l2，对应位相加
        if l1 != None:
            tmpsum += l1.val
            l1 = l1.next
        if l2 != None:
            tmpsum += l2.val
            l2 = l2.next
        tmp.val = tmpsum % 10     # 除10取余作为当前位的值
        tmpsum //= 10                #除10取整，即高位，作为指针的下个结点 进行加法运算
        if l1 == None and l2 == None and tmpsum == 0:
            break
        tmp.next = ListNode(0)
        tmp = tmp.next
    return ans

def mergeTwoNumbers(l1, l2):
    if l1 ==None and l2 ==None:
            return None
    ans = ListNode(0)
    tmp = ans
    while True:
        if l1 != None and l2 != None:
            if l1.val <= l2.val:
                tmp.val = l1.val
                l1 = l1.next
            else:
                tmp.val = l2.val
                l2 = l2.next  
        elif l1 == None and l2 !=None:
            tmp.val = l2.val
            if l2.next == None:
                break
            l2 = l2.next
        elif l2 == None and l1 !=None:
            tmp.val = l1.val
            if l1.next == None:
                break
            l1 = l1.next
        elif l1 == None and l2 == None:
            break
        
        tmp.next = ListNode()
        tmp = tmp.next 
    return ans

def main():  
    # print("Create a linklist")  
    # head=Creatlist(7)  
    # printlist(head)   
    # print("___________________________") 
    # print("Insert 9 after 3") 
    # insert(head,3,9)  
    # printlist(head)   
    # print("___________________________")
    # print("Delete 2") 
    # dellist(head,2)  
    # printlist(head)  
    # print("___________________________") 
    # print("afterappend 2") 
    # afterappend(head,2)  
    # printlist(head)   
    # print("___________________________") 
    # print("preappend 8") 
    # preappend(head,8)  
    # printlist(head) 
    l1 = Creatlist(3)
    l2 = Creatlist(4)
    # printlist(l1)
    printlist(l2)
    mergeTwoNumbers(l1,l2)
    printlist(l2)

if __name__=='__main__':  
    main()   # 主函数调用 