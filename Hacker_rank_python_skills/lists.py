#  12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


result_list = []
for i in range(int(input())):
    command,*args = input().split()
    if command == "print":
        print(result_list)
        continue
    for i in range(len(args)):
        args[i]=int(args[i])
    getattr(result_list,command)(*args)
