import random


def genRan(num):
    count=1
    numbers=[]
    while(count<=num):

        rand_number=random.randint(0,1000)
        
        numbers.append(rand_number)       
        count=count+1
    
    length=len(numbers)

    innerloop=0;
    outerloop=0;
    for outerloop in range(length):
        for innerloop in range(length-1):
            if numbers[innerloop] >= numbers[innerloop+1]:
                temp=numbers[innerloop]
                numbers[innerloop]=numbers[innerloop+1]
                numbers[innerloop+1]=temp
                
            innerloop+=1
        outerloop+=1
    
    return numbers
        

