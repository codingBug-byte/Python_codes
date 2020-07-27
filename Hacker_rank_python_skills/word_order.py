
# n  = int(input())
#
# myDict = {}
#
# for i in range(n):
#     inp = input()
#     if inp not in myDict:
#         myDict[inp] = 1
#     else:
#         myDict[inp] += 1
#
# print(len(myDict))
# print(*myDict.values())

from collections import Counter

counter = Counter([ input() for i in  range(int(input()))])
print(len(counter))
print(*counter.values())