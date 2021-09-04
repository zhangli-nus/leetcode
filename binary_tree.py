#coding: utf-8
from collections import defaultdict

global_node_index = 0

class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftnext = None
        self.rightnext = None
        self.index = global_node_index


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add_node(self, value):
        global global_node_index
        node = Node(value)
        global_node_index += 1
        if self.root is None:
            self.root = node
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.leftnext is None:
                    cur.leftnext = node
                    break
                else:
                    cur = cur.leftnext
            else:
                if cur.rightnext is None:
                    cur.rightnext = node
                    break
                else:
                    cur = cur.rightnext

    def tranverse_mid(self, ptr, res):
        if not ptr:
            return
        self.tranverse_mid(ptr.leftnext, res)
        res.append(ptr.value)
        self.tranverse_mid(ptr.rightnext, res)
        return res

    def tranverse_before(self, ptr, res):
        if not ptr:
            return
        res.append(ptr.value)
        self.tranverse_before(ptr.leftnext, res)
        self.tranverse_before(ptr.rightnext, res)
        return res

    def tranverse_after(self, ptr, res):
        if not ptr:
            return
        self.tranverse_after(ptr.leftnext, res)
        self.tranverse_after(ptr.rightnext, res)
        res.append(ptr.value)
        return res

    def tranverse_level(self):
        stack = []
        stack.append(self.root)
        res = []
        print("visit level")
        while stack:
            t = stack[0]
            stack = stack[1:]
            res.append(t.value)
            if t.leftnext:
                stack.append(t.leftnext)
            if t.rightnext:
                stack.append(t.rightnext)
        return res


    def visit_nonrecursive_before(self):
        stack = []
        v = self.root
        res = []
        while v is not None or len(stack) != 0:
            while v:
                res.append(v.value)
                stack.append(v)
                v = v.leftnext
            if stack:
                v = stack.pop()
                v = v.rightnext
        return res

    def visit_nonrecursive_middle(self):
        stack = []
        v = self.root
        res = []
        while v is not None or len(stack) != 0:
            while v:
                stack.append(v)
                v = v.leftnext
            if stack:
                v = stack.pop()
                res.append(v.value)
                v = v.rightnext
        return res

    def visit_nonrecursive_after(self):
        stack = []
        v = self.root
        is_visited = defaultdict(int)
        res = []

        # while v is not None or len(stack) != 0:
        #     while v:
        #         stack.append(v)
        #         is_visited[v.index] += 1
        #         v = v.leftnext
        #     if stack:
        #         v = stack.pop()
        #         if is_visited[v.index] == 2: #代表右节点已经访问过
        #             res.append(v.value)
        #             v = None
        #         else:
        #             stack.append(v)
        #             is_visited[v.index] += 1 #代表已经访问了右节点
        #             v = v.rightnext
        #             pass
        cur = self.root
        while (cur is not None or len(stack) > 0):
            while (cur):
                stack.append(cur)
                is_visited[cur.index] = 1
                cur = cur.leftnext
            if stack:
                v = stack.pop()
                if is_visited[v.index] == 1:
                    stack.append(v)
                    is_visited[v.index] += 1
                    cur = v.rightnext
                else:
                    res.append(v.value)

        return res


class BalancedBinaryTree(BinaryTree):
    def __init__(self):
        super(BalancedBinaryTree, self).__init__()
        self.root = None

    def getPtrDepth(self, ptr):
        if not ptr:
            return 0
        lef = self.getPtrDepth(ptr.leftnext)
        rgt = self.getPtrDepth(ptr.rightnext)
        return lef + 1 if lef > rgt else rgt + 1

    def getDepth(self):
        depth = self.getPtrDepth(self.root)
        return depth

    def getBalance(self):
        if not self.root:
            return True
        let = self.getPtrDepth(self.root.leftnext)
        rgt = self.getPtrDepth(self.root.rightnext)
        if abs(let - rgt) <= 1:
            return self.getBalance(self.root.leftnext) and self.getBalance(self.root.rightnext)
        else:
            return False

    def left_swift(self):
        a = self.root
        left_swift_node = self.root.leftnext.rightnext
        self.root = self.root.leftnext
        self.root.rightnext = a
        a.leftnext = left_swift_node

    def right_swift(self):
        a = self.root
        right_swift_node = self.root.rightnext.leftnext
        self.root = self.root.rightnext
        self.root.leftnext = a
        a.rightnext = right_swift_node


if __name__ == '__main__':
    b = BalancedBinaryTree()
    b.add_node(10)
    b.add_node(5)
    b.add_node(4)
    b.add_node(6)
    b.add_node(15)
    b.add_node(14)
    b.add_node(16)
    b.add_node(3)
    b.add_node(2)
    # b.visit()
    # b.visit_level()
    print("recursive before")
    res = b.tranverse_before(b.root, [])
    print(res)
    print("non-recursive before")
    res = b.visit_nonrecursive_before()
    print(res)
    print("recursive middle")
    res = b.tranverse_mid(b.root, [])
    print(res)
    print("non-recursive middle")
    res = b.visit_nonrecursive_middle()
    print(res)
    print("recursive after")
    res = b.tranverse_after(b.root, [])
    print(res)
    print("non-recursive after")
    res = b.visit_nonrecursive_after()
    print(res)
