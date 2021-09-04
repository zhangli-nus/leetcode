#coding: utf-8
import math

def adjust_heap(input_list, start, end):
    k = start
    while 2*(k+1)-1 <= end: #非叶子节点
        compare_idx = 2*(k+1)-1
        if compare_idx+1<=end and input_list[compare_idx]<input_list[compare_idx+1]: #右边的大，取右边的
            compare_idx = compare_idx+1
        if input_list[k] < input_list[compare_idx]:
            tmp = input_list[compare_idx]
            input_list[compare_idx] = input_list[k]
            input_list[k] = tmp
            k = compare_idx
        else:
            break
    pass

def heap_sort(input_list):
    length = len(input_list)
    start_idx = math.floor(length/2)-1
    while start_idx>=0:
        adjust_heap(input_list, start_idx, length-1)
        start_idx -= 1

    for idx in range(length-1, -1, -1):
        swap(input_list, idx, 0)
        adjust_heap(input_list, 0, idx-1)
    return input_list


def swap(input_list, a, b):
    tmp = input_list[b]
    input_list[b] = input_list[a]
    input_list[a] = tmp
    return input_list

if __name__ == '__main__':
    t = [50, 16, 30, 10, 60, 90, 2, 80, 70]
    res = heap_sort(t)
    print(res)
    pass