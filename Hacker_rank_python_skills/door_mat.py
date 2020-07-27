n,m = input().split()
n,m=int(n),int(m)
h = ".|."
for i in range(1,n,2):
    print((h*i).center(n*3,"-"))
print("welcome".center(n*3,"-"))
for i in reversed(range(1,n,2)):
    print((h*i).center(n*3,"-"))












