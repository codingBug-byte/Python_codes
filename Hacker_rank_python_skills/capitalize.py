def solve(s):
    s = input()

    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s

    # first, last = s.split()
    # first =first[0].upper() + first[1:]
    # last =last[0].upper() + last[1:]
    # s = first +" "+ last
    # print(s)

