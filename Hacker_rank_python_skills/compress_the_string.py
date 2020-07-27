from itertools import groupby
from collections import Counter

# s = input()
# k = []
# g = []
# for i,j in groupby(s):
#     k.append(i)
#     g.append(list(j))
# for i in range(len(g)):
#     print((len(g[i]),int(k[i])))

for k,g in groupby(input()):
    print((len(list(g)),int(k)),end=" ")