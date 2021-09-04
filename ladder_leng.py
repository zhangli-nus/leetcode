#coding: utf-8
# from collections import defaultdict
import copy

class TrieTree(object):
    def __init__(self):
        self.end = '/'
        self.root = dict()

    def add_word(self, word):
        cur = self.root
        for a in word:
            if a not in cur.keys():
                cur[a] = dict()
            cur = cur[a]
        cur[self.end] = word

    def add_words(self, words):
        for word in words:
            self.add_word(word)

    def search_word(self, word):
        cur = self.root
        for a in word:
            if a in cur.keys():
                cur = cur[a]
            else:
                return 0
        if self.end in cur:
            return 2 #exact match
        else:
            return 1 #prefix

    def search_one_mutation(self, word):
        res = []
        cur = self.root
        for idx, a in enumerate(word):
            candidate = cur.keys()
            if a in candidate:
                candidate.remove(a)
            for b in candidate:
                new_word = word[:idx]+b+word[idx+1:]
                res.append(new_word)
            if a in cur.keys():
                cur = cur[a]
            else:
                break
        new_res = []
        for t in res:
            if 2 == self.search_word(t):
                new_res.append(t)
        return new_res

class WordLadder(object):
    def __init__(self, begin_word, end_word, word_list):
        self.begin_word = begin_word
        self.end_word = end_word
        self.word_list = word_list
        self.trie_tree = TrieTree()

    def construct_trie(self):
        self.trie_tree.add_word(self.begin_word)
        self.trie_tree.add_words(self.word_list)

    def bfs(self):
        stack = []
        parent = dict((k, k) for k in self.word_list)
        parent[self.begin_word] = self.begin_word
        is_visited = dict()
        stack.append(self.begin_word)
        is_visited[self.begin_word] = 1
        while stack:
            cur_word = stack[0]
            stack = stack[1:]
            neighbors = self.trie_tree.search_one_mutation(cur_word)
            for neighbor in neighbors:
                if neighbor not in is_visited:
                    stack.append(neighbor)
                    is_visited[neighbor] = 1
                    parent[neighbor] = cur_word
                if neighbor == self.end_word:
                    break

        if self.end_word not in parent or parent[self.end_word] == self.end_word:
            return 0
        else:
            v = self.end_word
            route = 1
            while v!=self.begin_word:
                route+=1
                v = parent[v]
            return route



if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    wordList = ["hot", "dot", "dog", "lot", "log"]
    trie_tree = TrieTree()
    trie_tree.add_word(beginWord)
    trie_tree.add_words(wordList)
    t = copy.copy(wordList)
    t.append(beginWord)
    for word in t:
        res = trie_tree.search_one_mutation(word)
        print(word, res)
    t = WordLadder(beginWord, endWord, wordList)
    t.construct_trie()
    route = t.bfs()
    print(route)
    # ladder(beginWord, endWord, wordList)