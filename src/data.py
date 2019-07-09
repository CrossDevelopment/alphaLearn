import random

x=20

def genRan(i):
    y=0
    z=[]
    while(y<i):
        j=random.randint(y,i)
        z.append(j)       
        y=y+1
    
    length=len(z)

    for i in range(length):
        for j in range(0,length-i-1):
            if z[j] > z[j+1]:
                z[j], z[j+1] = z[j+1], z[j]


    
    
    return z
        
genRan(x)
