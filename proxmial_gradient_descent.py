#coding: utf-8

from scipy.optimize import minimize
import numpy as np
from collections import defaultdict
import time

e = 1e-10 # 非常接近0的值
fun = lambda x : (x[0] - 0.667) / (x[0] + x[1] + x[2] - 2) + sum(abs(x))# 约束函数
cons = ({'type': 'eq', 'fun': lambda x: x[0] * x[1] * x[2] - 1}, # xyz=1
        {'type': 'ineq', 'fun': lambda x: x[0] - e}, # x>=e，即 x > 0
        {'type': 'ineq', 'fun': lambda x: x[1] - e},
        {'type': 'ineq', 'fun': lambda x: x[2] - e}
       )

time_counter = defaultdict(str)
optimize_options = ['Nelder-Mead', 'CG', 'SLSQP', 'L-BFGS-B']
for option in optimize_options:
    s_time = time.time()
    x0 = np.array((1.0, 1.0, 1.0)) # 设置初始值
    res = minimize(fun, x0, method=option, constraints=cons)
    print('最小值：', res.fun)
    print('最优解：', res.x)
    print('迭代终止是否成功：', res.success)
    print('迭代终止原因：', res.message)
    time_counter[option] = time.time() - s_time
    print("used time: ", time_counter[option])

for key, value in time_counter.items():
    print(key, value)
