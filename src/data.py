import random

x=20

def genRan(num):
    count=1
    numbers=[]
    while(count<=num):
        rand_number=random.randint(count,num)
        numbers.append(rand_number)       
        count=count+1
    
    length=len(rand_number)

    innerloop=0;
    outerloop=0;
    while outerloop<length:
        while innerloop<length:
            if numbers[innerloop] > numbers[innerloop+1]:
                numbers[innerloop], numbers[innerloop+1] = numbers[innerloop+1], numbers[innerloop]
            innerloop+=1
        outerloop+=1
    
    
    return numbers
        

