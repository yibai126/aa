def findMinAndMax(L):
    min_val = None
    max_val = None
    for i in L:
        if isinstance(i, (int, float)):
            if min_val is None or i < min_val:
                min_val = i
            if max_val is None or i > max_val:
                max_val = i
    return min_val, max_val

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')