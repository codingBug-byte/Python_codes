from collections import Counter
n =int(input())
sizes = Counter(list(map(int,input().split())))
sum = 0
print(sizes)
for i in range(int(input())):
    size,price=map(int,input().split())
    if size in sizes.keys() and sizes[size]>0:
        sum += price
        sizes[size] -=1
        print(sizes)

print(sum)