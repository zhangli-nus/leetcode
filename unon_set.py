#coding: UTF-8
from collections import defaultdict

#牢记三个点
#1. Graph的数据节奏，点和边
#2. 构造一个parent数据集。初始化当前父亲节点为自己，后续有一条边的时候，一直找到根(一定是当前parent等于当前的值)，然后把当前parent改成target的即可
#3. 最后找联通子图的时候，每个节点都去找它的根节点，然后返回即可
class Graph(object):
    def __init__(self):
        pass

    def construct_graph(self, words):
        self.vertex = []
        self.edges = []
        for word in words:
            for alpha in word:
                if alpha not in self.vertex:
                    self.vertex.append(alpha)
        for word in words:
            for i in range(len(word)-1):
                self.edges.append((word[i],word[i+1]))
        pass

    def find_parent(self, parent, i):
        j = i
        while parent[j] != j:
            j = parent[j]
        return j

    def find_mts(self, words):
        self.construct_graph(words)
        parent = dict()
        for vertex in self.vertex: #每个节点否赋予自己
            parent[vertex] = vertex
        for edge in self.edges:
            i, j = edge
            x = self.find_parent(parent, i)
            y = self.find_parent(parent, j)
            if x == y:
                continue
            elif x < y:
                parent[x] = y
            else:
                parent[y] = x

        disjoint_set = defaultdict(list)
        for vertex in self.vertex:
            y = self.find_parent(parent, vertex)
            disjoint_set[y].append(vertex)

        return disjoint_set

if __name__ == '__main__':
    words = [['f', 'g'], ['t', 'k', 's'],['a', 'b', 'c'], ['c', 'e', 'k'], ['m', 'n']]
    g = Graph()
    disjoint_set = g.find_mts(words)
    print(disjoint_set)