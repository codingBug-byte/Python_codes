l =[i for i in input()]
count = 0
stack = []
flag = 0
ct = 0
mode = ["{", "[", "(", ")", "]", "}"]
for i in range(len(l)):
   if l[i] in mode[:3]:

       stack.append(l[i]);
       flag = 1
   elif len(stack) != 0:

       c = stack.pop()
       if l[i] == ')'and c =='(':
           count+=1
       elif l[i] == '}'and c=='{':
           count += 1
       elif l[i]== ']' and c =='[':
           count+=1
       elif l[i] == '*' and l[i+1]=='*':
           ct = 1
           stack.append(c)

       elif l[i] =="*":

           stack.append(c)
           continue






if ct == 1:
    print("{} {}".format("Yes",count))
else:
    print("{} {}".format("No",count))
