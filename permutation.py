#coding: utf-8
import copy

class permuatation(object):
    def __init__(self):
        pass


    def permute(self, words):
        if len(words)<=1:
            return words
        alphabet = words[0]
        remaining = words[1:]
        res = self.permute(remaining)

        pass

if __name__ == '__main__':
    t = permuatation()
    res = t.permute('aaabcd')