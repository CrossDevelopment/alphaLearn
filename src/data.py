import random

x=20

def genRan(i):
    y=0
    z=[]
    while(y<i):
        j=random.randint(y,i)
        z.append(j)       
        y=y+1
    
    return z
        
genRan(x)
