# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
#


for _ in range(int(input())):
    x = int(input())
    a = set(input().split())
    y = int(input())
    b = set(input().split())
    if a.issubset(b):
        print("True")
    else:
        print("False")



