def addNum(n):
    return n * addNum(n-1) if n>1 else 1
print(addNum(8)) #24