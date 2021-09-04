#coding: utf-8
from collections import defaultdict
from functools import reduce


class DirectedGraph(object):
    def __init__(self):
        self.vertex = []
        self.edge = defaultdict(list)

    def verify_word_lists(self, word_lists):
        word_start = defaultdict(list)
        for word in word_lists:
            word_start[word[0] + word[-1]].append(word)  # 去掉aab, ab中的一个

        new_word_lists = []
        for key, value in word_start.items():
            word = reduce(lambda x, y: x if len(x) > len(y) else y, value)
            new_word_lists.append(word)
        return new_word_lists

    def construct_graph(self, word_lists):
        word_lists = self.verify_word_lists(word_lists)
        word_lists = sorted(word_lists, key=lambda x: x[0], reverse=False)
        self.vertex = word_lists
        for idx in range(len(word_lists)):
            idy = idx + 1
            for idy in range(idx + 1, len(word_lists)):
                if word_lists[idx][-1] <= word_lists[idy][0]:
                    break
            self.edge[word_lists[idx]].extend(word_lists[idy:])

    def get_node_max_len(self):
        word_length = defaultdict(int)  # 保留计算过的node开始的最大长度的长度
        word_is_computed = defaultdict(int)  # 保留计算过的node开始的最大长度
        temp = []
        for word in self.vertex:
            temp.append(self.get_node_len(word, word_length, word_is_computed))
        return word_length

    def get_node_len(self, word, word_length, word_is_computed):
        temp = []
        for edge in self.edge[word]:
            if word_is_computed[edge]:
                temp.append(word_length[edge])
            else:
                temp.append(self.get_node_len(edge, word_length, word_is_computed))
        if temp:
            word_length[word] = len(word) + max(temp)
        else:
            word_length[word] = len(word)
        word_is_computed[word] = 1
        return word_length[word]


if __name__ == '__main__':
    n = 4
    word_lists = ['aaa', 'aa', 'bcd', 'bd', 'zzz', 'bcdef']
    a = DirectedGraph()
    a.construct_graph(word_lists)
    word_length = a.get_max_length()
    print word_length
