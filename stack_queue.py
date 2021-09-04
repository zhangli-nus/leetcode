# coding: utf-8


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):  # 进栈
        self.stack.append(value)
        return value

    def pop(self):  # 出栈
        if self.stack:
            return self.stack.pop()
        else:
            raise LookupError("stack is empty")

    def is_empty(self):  # 如果栈为空
        return bool(self.stack)

    def top(self):
        # 取出目前stack中最新的元素
        return self.stack[-1]


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Queue:

    def __init__(self):
        self.rear=None
        self.front=None
        self.r=0
        self.f=0

    def isEMpty(self):
        if self.r==self.f:
            print("The queue is empty")
        else:
            print("The queue is not empty")

    def push(self,data):
        if self.f==self.r:
            q=Node(data)
            self.rear=q
            self.front=q
            self.f=0
            self.r=1
        else:
            q=Node(data)
            self.rear.next=q
            self.rear=q
            self.r+=1

    def pop(self):
        if self.r==self.f:
            print("The Queue is empty")
            #return false
        else:
            self.front=self.front.next
            self.f=self.f+1

    def top(self):
        if self.r==self.f:
            print("empty")
        else:
            print(self.front.data)


if __name__ == '__main__':
    a = Stack()
    a.push(1)
    a.push(2)
    print("top", a.top())
    print(a.pop())
    b = Queue()
    b.push(1)
    b.push(2)
    print("top", b.top())
    print("pop", b.pop())