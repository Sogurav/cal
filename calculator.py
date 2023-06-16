n1=1
while n1 == 1: 
    print("Choose any of given option")
    print ("1) Add \n2)Subtract\n3)multiplication\n4)Division")
    num=int(input("Enter Number:"))
    if num == 1: 
        a=float(input("Enter first Number :")) 
        b=float(input("Enter second Number :")) 
        print("Addition is : ",(a+b)) 
    elif num==2: 
        a=float(input("Enter first Number :")) 
        b=float(input("Enter second Number :")) 
        print("Subtraction is : ",(a-b)) 
    elif num==3 : 
        a=float(input("Enter first Number :")) 
        b=float(input("Enter second Number :")) 
        print("Multiplication is : ",(a*b)) 
    elif num==4: 
        a=float(input("Enter first Number :")) 
        b=float(input("Enter second Number :")) 
        print("Division is : ",(a/b)) 
    else: 
        print("Wrong choice") 
    n=input("If you want to continue press 1 \n otherwise press any key ") 
    if n!="1": 
        exit()
    n1=int(n)