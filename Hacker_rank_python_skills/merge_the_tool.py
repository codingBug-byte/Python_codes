
# from collections import OrderedDict
# def merge_the_tools(string, k):
#     substrings = [ string[i:i+k] for i in range(0,len(string),k)]
#     for i in range(len(substrings)):
#         substrings[i] = "".join(OrderedDict.fromkeys(substrings[i]))
#     for i in substrings:
#         print(i)


S, N = input(), int(input())
print(list(iter(S)))
print(list(zip(*[iter(S)] * N)))
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)