 # -*- coding: utf-8 -*-
import time

def partial_table1(p):
    prefix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = [p[j:i+1] for j in range(1, i+1)]
        intersection = prefix.intersection(set(postfix))
        if intersection:
            ret.append(max(map(lambda x: len(x), intersection)))
        else:
            ret.append(0)
    return ret


def kmp_match(a, p):
    m, n = len(a), len(p)
    cur = 0
    table = partial_table1(p)
    while cur <= m-n:
        for i in range(n):
            if a[i+cur] != p[i]:
                cur += max(i-table[i-1], 1)  #有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        if i == n-1:
            return cur
    return -1

start_time = time.time()
a = "abbabaaaabbbaabaabaabbbaaabaaaaaabbbabbaabbabaabbabaaaaababbabbaaaaabbbbaaabbaaabbbbabbbbaaabbaaaaababbaababbabaaabaabbbbbbbaabaabaabbbbababbbababbaaababbbabaabbaaabbbba"*100
# a = "abbbbbbaaaa"
p = "bbbbbbaa"
print(partial_table1(p))
t = kmp_match(a, p)
if t==-1:
    print("cannot match")
else:
    print(a[t:t + len(p)])
    print(p)
    print(t)
print(time.time()-start_time)