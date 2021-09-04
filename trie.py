# coding: utf-8
from collections import defaultdict


class Trie(object):
    def __init__(self):
        self.end = '/'
        self.root = defaultdict(dict)

    def construct_word(self, word):
        cur = self.root
        for alpha in word:
            if alpha not in cur.keys():
                cur[alpha] = {}
            cur = cur[alpha]
        cur[self.end] = dict()

    def construct_words(self, words):
        for word in words:
            self.construct_word(word)

    def traverse(self, input_dict):
        tmp = []
        for key in input_dict.keys():
            if key == self.end:
                tmp.append("")
            res = self.traverse(input_dict[key])
            tmp.extend([key + ele for ele in res])
        return tmp

    def search(self, word):
        cur = self.root
        for alpha in word:
            if alpha in cur:
                cur = cur[alpha]
            else:
                return False
        return True

    def find_word(self, word):
        cur = self.root
        for alpha in word:
            if alpha in cur:
                cur = cur[alpha]
            else:
                return False
        if self.end in cur:
            return True
        else:
            return False


if __name__ == '__main__':
    words = ["this", "thi", "real", "hard", "trh", "hea", "iar", "sld"]
    trie = Trie()
    trie.construct_words(words)
    print(trie.root)
    words = trie.traverse(trie.root)
    print(words)
    print(trie.find_word("this"))
    print(trie.find_word("th"))
