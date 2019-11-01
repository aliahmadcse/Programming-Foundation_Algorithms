# the node class
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList():
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # insert a node at head
        newNode = Node(data)
        newNode.set_next(self.head)
        self.head = newNode
        self.count += 1

    def find(self, val):
        # find the first occurence of val
        item = self.head
        while (item != None):
            if (item.get_data() == val):
                return item
            item = item.get_next()
        return None

    def deleteAt(self, index):
        # deleting a node at a particular index
        if index > self.count-1:
            return
        # if the node to be deleting is the head node
        if index == 0:
            tempHead = self.head
            self.head = self.head.get_next()
            tempHead.get_next = None
        else:
            tempIndex = 0
            node = self.head
            while tempIndex < index-1:
                node = node.get_next()
                tempIndex += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        # print all the node's data
        tempNode = self.head
        while(tempNode != None):
            print(f"Node: {tempNode.get_data()}")
            tempNode = tempNode.get_next()


itemlist = LinkedList()
# inserting some nodes
itemlist.insert(10)
itemlist.insert(12)
itemlist.insert(14)
itemlist.insert(16)
# printing  the values
itemlist.dump_list()


print(itemlist.get_count())
# print(itemlist.find(12))
# print(itemlist.find(78))

# deleting items
itemlist.deleteAt(2)
itemlist.dump_list()
print(itemlist.get_count())
