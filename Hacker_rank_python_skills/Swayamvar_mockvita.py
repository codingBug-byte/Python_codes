from queue import Queue

def check(grooms,brides):
    count = 0
    while(grooms.empty()):
        if ( grooms.get()== brides.get()):
            count+=1
        else:










n = int(input())
brides = Queue(maxsize=n)
grooms = Queue(maxsize=n)
inputs =[i for i in input()]
for i in range(n):
    brides.put(inputs[i])
inputs1 =[i for i in input()]
for i in range(n):
    grooms.put(inputs[i])


check(grooms,brides)



