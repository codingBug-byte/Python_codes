def solve(s):
    s = input()

    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s

   
