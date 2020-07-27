# eng = set()
# eng_students = int(input())
# l = input().split()
# for i in range(eng_students):
#     eng.add(int(l[i]))
# phy = set()
# phy_students = int(input())
# k = input().split()
# for i in range(phy_students):
#     phy.add(int(k[i]))
#
# print(eng.symmetric_difference(phy))



_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.symmetric_difference(b)))