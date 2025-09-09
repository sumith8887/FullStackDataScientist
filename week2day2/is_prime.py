def is_prime(num):
    factors=1
    if(num>=2):
        for i in range(2,num+1):
            if(num%i==0):
                factors+=1
        if(factors>2):
            return False
        else:
            return True
    else:
        return False

n=int(input("Enter the number : "))
flag=is_prime(n)
if(flag):
    print("Prime Number")
else:
    print("Not a prime number")