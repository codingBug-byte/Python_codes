# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10

# def fun( n ):
#     return n*n
# k,m = map(int,input().split())
# sum = 0
# for i in range(k):
#     key,*val = map(int,input().split())
#     sum += fun(max(val))
#
#
#
# print(sum % m)

from itertools import product

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
print(list(product(*N)))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))