n=int(input("Enter the number of units : "))
bill=0
if(n>0):
    if(n<100):
        bill+=n*5
    elif(n>=100):
        bill+=100*5
        n=n-100
if(n>0):
    if(n<100):
        bill+=n*7
    elif(n>=100):
        bill+=100*7
        n=n-100
if(n>0):
    bill+=n*10
print(bill)