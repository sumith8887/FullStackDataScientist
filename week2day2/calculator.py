while(True):
    n=int(input("Enter Your Choice : 1.Add 2.sub 3.mul 4.div 5.Exit  : "))
    if(n==1):
        a=int(input("Enter first Value :"))
        b=int(input("Enter second Value :"))
        print(a+b)
    elif(n==2):
        a=int(input("Enter first Value :"))
        b=int(input("Enter second Value :"))
        print(a-b)
    elif(n==3):
        a=int(input("Enter first Value :"))
        b=int(input("Enter second Value :"))
        print(a*b)
    elif(n==4):
        a=int(input("Enter first Value :"))
        b=int(input("Enter second Value :"))
        print(a/b)
    else:
        print("Exiting the Calculator")
        break
