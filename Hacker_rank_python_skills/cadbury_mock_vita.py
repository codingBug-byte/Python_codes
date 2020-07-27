mil, mal, miw, maw = int(input()), int(input()), int(input()), int(input())
d = {}
count = 0
for i in range(mil,mal+1):
    for j in range(miw,maw+1):
        t_l, t_b=i, j
        c = 0
        if (t_l, t_b) in d:
            c = d[t_l, t_b]
        else:
            while t_l != 0 and t_b != 0:
                if (t_l, t_b) in d:
                    c += d[t_l, t_b]
                    break
                else:
                    max_val,min_val = max(t_l,t_b),min(t_l,t_b)

                    if max_val % min_val == 0:
                        c+=max_val/min_val
                        break
                    else:
                        t_l = min_val
                        t_b = max_val - min_val
                        c += 1
                d[i, j]= c
                d[j, i] = c
            count += c

print(int(count),end ="")







