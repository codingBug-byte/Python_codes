# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2
def compare( cubes ):
    upper, lower = 0, len(cubes)-1
    ontop = max(cubes)
    # print(upper)
    # print(lower)
    # print(cubes)

    while not ( upper == lower):
        #print("yess")
        if cubes[upper] >= cubes[lower]:
            if upper <= ontop:
                ontop = cubes[upper]
                #print(ontop)
                upper += 1
               # print(upper)
            else :
                return False
        else:
            if cubes[lower] <= ontop:
                #print("yesss")
                #print(cubes[lower])
                ontop = cubes[lower]
                lower -= 1
                #print(lower)
               # print(ontop)
            else :
                return False

    return True

for i in range(int(input())):
    k = input()
    cube_number = list(map(int, input().split()))
    if compare(cube_number) == False:
        print("NO")
    else:
        print("YES")





from collections import defaultdict,deque
T = input()
D = defaultdict(list)
# Function to check ascending order
def ordAsc(A):
    return all(A[i] <= A[i+1] for i in range(len(A)-1))

for i in xrange(T):
    k = input()
    D[i].append(map(int,raw_input().split()))

for y in D:
    l = D[y][0].index(min(D[y][0]))
    if ordAsc(D[y][0][l:]):
        print 'Yes'
    else:
        print 'No'