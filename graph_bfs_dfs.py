# coding: utf-8
from collections import defaultdict

class Graph(object):
    def __init__(self, word_lists):
        self.graph = dict()
        self.construct_graph(word_lists)
        pass

    def construct_graph(self, word_lists):
        word_keys = self.get_keys(word_lists)
        for vertex in word_keys:
            self.add_vertex(vertex)
        for word_list in word_lists:
            for idx in range(0, len(word_list)-1):
                self.add_edge(word_list[idx], word_list[idx+1])

    def print_graph(self):
        for key in self.graph:
            print("{key}, {value}".format(key=key, value=self.graph[key]))

    def add_vertex(self, word_key):
        if word_key not in self.graph:
            self.graph[word_key] = []

    def add_edge(self, v1, v2):
        '''without order'''
        if v2 not in self.graph[v1]:
            self.graph[v1].append(v2)
        if v1 not in self.graph[v2]:
            self.graph[v2].append(v1)

    def get_keys(self, word_lists):
        word_keys = set()
        for word_list in word_lists:
            for word in word_list:
                word_keys.add(word)
        return word_keys

    def BFS(self, node):
        queue, order = [], []
        queue.append(node)
        order.append(node) #BFS访问一个即保留一个
        visited_sign = defaultdict(int)
        visited_sign[node] = 1
        while queue:
            node = queue.pop()
            neighbors = self.graph[node]
            for neighbor in neighbors:
                if visited_sign[neighbor] == 0:
                    queue.append(neighbor)
                    order.append(neighbor)
                    visited_sign[neighbor] = 1
        return order

    def DFS(self, node):
        queue, order = [], []
        queue.append(node)
        visited_sign = defaultdict(int)
        while queue:
            node = queue.pop()
            visited_sign[node]=1
            order.append(node)
            neighbors = self.graph[node]
            for neighbor in neighbors:
                if visited_sign[neighbor] == 0:
                    queue.append(neighbor)
                    visited_sign[neighbor] = 1
        return order


    def find_all_mts(self):
        nodes = list(self.graph.keys())
        res = []
        while nodes:
            node = nodes[0]
            order = self.DFS(node)
            res.append(order)
            for t in order:
                if t in nodes:
                    nodes.remove(t)
        return res


if __name__ == '__main__':
    word_lists = [['a', 'b', 'c', 'd'], ['e', 'f', 'g'],
                  ['h', 'i', 'j'], ['i', 'k'], ['e', 'i', 'g']]
    g = Graph(word_lists)
    g.print_graph()
    res = g.find_all_mts()
    print(res)