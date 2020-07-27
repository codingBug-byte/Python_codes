import textwrap
def wrap1(string, max_width):
    empty = ""
    rr=textwrap.wrap(string,max_width)
    for i in rr:
        empty = empty + i + "\n"
    return empty
    # s = ""
    # for c in range(0,len(string),max_width):
    #     s += string[c:c+max_width] + "\n"
    # return s



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap1(string, max_width)
    print(result)