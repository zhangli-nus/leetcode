#coding: utf-8
import copy

def findsubword(query, vocab):
    if not query:
        return True

    res = []
    for word in vocab:
        if query[0:len(word)] == word:
            print('%s, %s'%(word, query[len(word):]))
            res.append(findsubword(query[len(word):], vocab))
    if res and res.count(True)!=0:
        return True
    else:
        return False

def findall(word_lists):
    word_lists = sorted(word_lists, key=lambda x: len(x), reverse=True)
    print(word_lists)
    for i in range(len(word_lists)):
        query = word_lists[i]
        vocab = copy.copy(word_lists)
        vocab.remove(query)
        if findsubword(query, vocab) == True:
            return query
    return 0


if __name__ == '__main__':
    t = ["test", "tester", "testertest", "testing", "testingtester"]
    query = findall(t)
    print(query)