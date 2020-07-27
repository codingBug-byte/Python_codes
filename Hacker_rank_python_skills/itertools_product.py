from itertools import product
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
print(*tuple(product(list1,list2)))
