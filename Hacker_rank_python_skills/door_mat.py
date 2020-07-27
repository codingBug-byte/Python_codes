n,m = input().split()
n,m=int(n),int(m)
h = ".|."
for i in range(1,n,2):
    print((h*i).center(n*3,"-"))
print("welcome".center(n*3,"-"))
for i in reversed(range(1,n,2)):
    print((h*i).center(n*3,"-"))












#
# n = int(input())
# dec = []
# for i in range(1,int(n**0.5)):
#     if n%i == 0:
#         print(i,end = " ")
#         if not ( n / i == i):
#             dec.append(int( n / i))
# dec.sort()
# for i in dec:
#     print(i,end = " ")