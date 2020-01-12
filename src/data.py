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
    while outerloop<length:
        while innerloop<length:
            if numbers[innerloop] > numbers[innerloop]:
                numbers[innerloop], numbers[innerloop] = numbers[innerloop+1], numbers[innerloop]
            innerloop+=1
        outerloop+=1
    
    
    return numbers
        

