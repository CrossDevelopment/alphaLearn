import data
import random
from template.traindata import template

def main():
    num = int(input("Enter an integer: "))
    list=data.genRan(num)
    template(list)
    

if __name__ == "__main__":
    main()
