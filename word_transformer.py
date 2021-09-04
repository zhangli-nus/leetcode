# coding: utf-8

class Trie(object):
    def __init__(self):
        self.END = '/'
        self.root = dict()

    def add_word(self, word):
        cur = self.root
        for alpha in word:
            if alpha not in cur:
                cur[alpha] = dict()
            cur = cur[alpha]
        cur[self.END] = {}

    def search(self, word):
        cur = self.root
        for alpha in word:
            if alpha not in cur:
                return 0 #non-prefix
            cur = cur[alpha]
        if self.END in cur:
            return 1 #exact match
        else:
            return 2 #prefix

    def add_words(self, words):
        for word in words:
            self.add_word(word)

    def search_mutate_one(self, query):
        mutate = []
        cur = self.root
        for idx, alpha in enumerate(query):
            new_alpha = cur.keys()
            if alpha in new_alpha:
                new_alpha.remove(alpha)
            if self.END in new_alpha:
                new_alpha.remove(self.END)
            for t in new_alpha:
                mutate.append(query[0:idx]+t+query[idx+1:])
            if alpha in cur:
                cur = cur[alpha]
            else:
                break
        res = []
        for word in mutate:
            if self.search(word) == 1:
                res.append(word)

        return res

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[str]
        """
        start_word = beginWord
        end_word = endWord
        word_lists = wordList
        if end_word not in word_lists:
            return []
        else:
            full_word_lists = self.get_full(start_word, word_lists)

        trie = Trie()
        trie.add_words(full_word_lists)

        parents = dict()
        for word in full_word_lists:
            parents[word] = word

        parents = self.dfs(start_word, end_word, parents, trie)
        res = self.find_path(start_word, end_word, parents)
        return res


    def find_path(self, start_word, end_word, parents):
        res = []
        j = end_word
        while parents[j]!=j:
            res.append(j)
            j = parents[j]
        res.append(j)
        if j!=start_word:
            return []
        else:
            res.reverse()
        return res


    def dfs(self, start_word, end_word, parents, trie):
        stack = [start_word]
        is_visited = {start_word: 0}
        while len(stack) > 0:
            node = stack.pop()
            neighbors = trie.search_mutate_one(node)
            for neighbor in neighbors:
                if neighbor not in is_visited and neighbor not in stack:
                    parents[neighbor] = node
                    stack.append(neighbor)
                    is_visited[neighbor] = 0
                    if neighbor == end_word:
                        return parents
        return parents

    def get_full(self, start_word, word_lists):
        new_lists = [start_word]
        new_lists.extend(word_lists)
        return list(set(new_lists))