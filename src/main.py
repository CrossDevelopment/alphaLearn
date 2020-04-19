import data
import random
import filehandler

def main():
    num = int(input("Enter an integer: "))
    list=data.genRan(num)
    print(list)
    filehandler.fileWrite('bst.txt',list)

if __name__ == "__main__":
    main()
