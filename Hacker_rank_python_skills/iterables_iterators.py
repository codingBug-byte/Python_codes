
#the question isnt clear as of now so tried yet as to pass the challenge just did the below solution
from itertools import combinations
# n = input()
# l = list(input().split())
# k = int(input())
# print(l)
#
# count = 0
# p = list(combinations(sorted(l),k))
#
# print(p)
#
# for i in range(k -1 ) :
#     for j in p:
#         if l[i] in j :
#             count +=1
# print(count)


N = int(input()); a = input().split(); K = int(input())
c = list(combinations(a,K))
result = [1 for i in range(len(c)) if 'a' in c[i]]
print(sum(result)/len(c))