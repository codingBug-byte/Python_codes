

#solution1
def print_formatted(number):
    space = len(f"{number:b}")
    for i in range(1,number+1):
        print(f"{i:{space}d} {i:{space}o} {i:{space}X} {i:{space}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#solution 2

# n = int(input())
#
# results = []
#
# for i in range(1, n+1):
#     decimal = str(i)
#     octal = str(oct(i)[2:])
#     hex_ = str(hex(i)[2:]).upper()
#     binary = str(bin(i)[2:])
#
#     results.append([decimal, octal, hex_, binary])
# print(results)
#
# width = len(results[-1][3])
# print(len(results[-1][3]) )# largest binary number
#
# for i in results:
#     print(*(rep.rjust(width) for rep in i))