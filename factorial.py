#coding: utf-8
import math

def get_num(n):
    pick_k_combination = [0]*n
    total = math.factorial(n) #
    for k in range(n):
        pick_num = k + 1
        pick_k_combination[k] = total/(math.factorial(pick_num-1)*math.factorial(n-pick_num))
    return int(sum(pick_k_combination)%(1e9+7))


if __name__ == '__main__':
    n = 3
    print(get_num(n))


