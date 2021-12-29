
class DoubleLinkedList():
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None,
            "pre": None,
        }
        self.tail = self.head
        self.lenth = 1

    def append(self, value):
        newNode = {
            "value": value,
            "next": None,
            "pre": None,
        }
        newNode["pre"] = self.tail
        self.tail["next"] = newNode
        self.tail = newNode
        self.lenth += 1 
        return self 

    def preappend(self, value):
        newNode = {
            "value": value,
            "next": None,
            "pre": None,
        }

        newNode["next"] = self.head
        self.head["pre"] = newNode
        self.head = newNode
        self.lenth += 1
        return self

    def insert(self, index, value):
        newNode = {
            "value": value,
            "next": None,
            "pre": None,
        }

        leader = self.traverseToIndex(index-1)
        holdingPointer = leader["next"]
        leader["next"] = newNode
        newNode["next"] = holdingPointer

        self.lenth += 1
        return self

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode["next"]
            counter += 1
        return currentNode

    def delete(self, index):
        leader = self.traverseToIndex(index-1)
        follower = self.traverseToIndex(index+1)
        leader["next"] = follower
        self.lenth -= 1
        return self

    def getnums(self):
        mylist = []
        currentNode = self.head
        while currentNode != None:
            mylist.append(currentNode['value'])
            currentNode = currentNode['next']
        return mylist

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = first["next"]
        while second:
            tmp = second["next"]
            second["next"] = first
            first = second
            second = tmp
        
        self.head["next"] = None
        self.head = first
        return self.getnums()


myLinkedList = DoubleLinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.preappend(1)
myLinkedList.insert(2,9)
myLinkedList.insert(3,9)
myLinkedList.delete(2)
myLinkedList.delete(2)
print(myLinkedList.getnums())
print(myLinkedList.reverse())
# attrs = vars(myLinkedList)
# print(attrs)


