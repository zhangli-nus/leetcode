#coding: utf-8
import numpy as np

def find_value(input):
    n = len(input)
    t = [0]*n
    t[0] = input[0]
    action = [0] * n
    for i in range(1, n):
        t[i] = max(t[i-1]+input[i], input[i])
        if t[i-1]+input[i] <= input[i]:
            action[i] = 1
        else:
            action[i] = 0
    return t, action

if __name__ == '__main__':
    t = [-5, -4, 3, -2, 10, 8, -5, 8, -20]
    seq, action = find_value(t)
    print(max(seq))
    print(seq)
    idx = np.argmax(seq)
    sub_seq = []
    print(action)
    for i in range(idx, -1, -1):
        if action[i] == 1: #重新开始
            sub_seq.append(t[i])
            break
        else:
            sub_seq.append(t[i]) #使用前面的和
    print(sub_seq)