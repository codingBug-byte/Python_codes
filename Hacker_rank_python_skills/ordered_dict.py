
from collections import OrderedDict,defaultdict
od = OrderedDict()
m = defaultdict(list)
for i in range(int(input())):
    k = input().split()

    k[0] = ' '.join(k[0:len(k)-1])

    k[1] = int(k[len(k)-1])

    k = k[0:2]

    m[k[0]].append(k[1])
    od[k[0]] = i
print(od)
print(m)
for i in od:
    print(i, sum(m[i]))

