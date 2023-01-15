#define the functions needed, add, sub, div, mul
#print options to the user
#ask for values
#call the functions
#while loop to continue the program until the user wants to exit 

def add(a,b):
    answer=a+b
    print(str(a)+ "+"+str(b)+"="+str(answer)+"\n")
    # print(a+b)

def sub(a,b):
    answer=a-b
    print(str(a)+"-"+str(b)+"="+str(answer)+"\n")
    # print(a-b)

def mul(a,b):
    answer=a*b
    print(str(a)+"*"+str(b)+"="+str(answer)+"\n")
    # print(a*b)

def div(a,b):
    answer=a/b
    print(str(a)+"/"+str(b)+"="+str(answer)+"\n")
    # print(a/b)

while True:
    print("A. ADDITION")
    print("B. SUBTRACTION")
    print("C. MULTIPLICATION")
    print("D. DIVISION")
    print("E. EXIT")

    choice=input("input your choice")

    if choice =="a" or choice=="A":
        print("ADDITION")
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        add(a,b)
    elif choice=="b" or choice=="B":
        print("SUBTRACTION")
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        sub(a,b)
    elif choice=="c" or choice=="C":
        print("MULTIPLICATION")
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        mul(a,b)
    elif choice=="d" or choice=="D":
        print("DIVISION")
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        div(a,b)
    elif (choice=="e" or "E"):
        print("PROGRAM ENDED")
        quit()






