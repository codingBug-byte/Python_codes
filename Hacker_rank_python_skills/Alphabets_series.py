n =int(input())
if n >=1 and n<=26:
    print(chr(64+(n)))
else:
    c = n//26
    re = n%26
    print(chr(64+c)+chr(64+re))


