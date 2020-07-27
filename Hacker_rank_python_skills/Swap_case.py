


# HackerRank.com presents "Pythonist 2".







def swap_case(case ):
    swapp =''

    for i in  range(len(case)):

        if case[i].isupper():
           swapp += case[i].lower()

        else:
            swapp += case[i].upper()


    return swapp


if __name__ == '__main__':
    case = input()
    print(swap_case(case))

