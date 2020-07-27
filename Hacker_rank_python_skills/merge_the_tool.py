S, N = input(), int(input())
print(list(iter(S)))
print(list(zip(*[iter(S)] * N)))
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
