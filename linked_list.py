#coding: utf-8

class LinkedNode(object):
    def __init__(self, value):
        self.value = value
        self.nextval = None
        pass

class LinkedList(object): #其实只需要保留一个head指针
    def __init__(self):
        self.headval = None
        pass

    def add_node(self, value):
        node = LinkedNode(value)
        if self.headval == None:
            self.headval = node
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = node

    def show(self):
        cur = self.headval
        while cur:
            print(cur.value)
            cur = cur.nextval


li = LinkedList()
li.add_node(10)
li.add_node(11)
li.add_node(12)
li.add_node(13)
li.show()