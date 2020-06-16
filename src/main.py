import data
import random

def main():
    num = int(input("Enter an integer: "))
    list=data.genRan(num)
    print(list)
   
    print(len(list))

if __name__ == "__main__":
    main()
