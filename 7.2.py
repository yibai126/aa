def findMinAndMax(L):
    if L==[]:
        return (None, None)
    else:
        max=L[0]
        min=L[0]
        for x in L:
            if isinstance(x, (int, float)):
                if x < min:
                    min = x
                if x > max:
                    max = x
            
        return min, max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试1失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试2失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试3失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试4失败')
else:
    print('测试成功!')
