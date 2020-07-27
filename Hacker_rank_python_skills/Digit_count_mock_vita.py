def rule1(l):
    rule_list=[]

    c=[]
    sum = 0
    for i in l:
        c =[int(j) for j in i]

        sum =str(max(c)*11+min(c)*7)
        if len(sum) > 2:
            rule_list.append(sum[len(sum)-2:])

        else:
            rule_list.append(str(sum))

        c.clear()
        sum = 0
    return rule_list

def rule2( l):
    count = 0
    c = rule1(l)
    even_positin=[0]*10
    odd_position = [0]*10
    for i in range(len(c)):
        msb = int(c[i][0])
        if i%2 != 0:

            even_positin[msb]+=1
        else :
            odd_position[msb]+=1

    for i in range(10):
        if even_positin[i]>= 1 and even_positin[i] <= 3:
            count+=(even_positin[i]-1)
    for i in range(10):
        if odd_position[i]>=1 and odd_position[i]<= 3:
            count+=(odd_position[i]-1)



    print(count ,end ="")





l =input().split()
l=l[1:]

rule2(l)