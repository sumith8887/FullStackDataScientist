def is_prime(num):
    counter=0
    if(num>=2):
        for i in range(2,num+1):
            if(num%i==0):
                counter=counter+1
        if(counter<2):
            return True
        else:
            return False

n=int(input())
primes_list=[]
for i in range(2,n+1):
    is_prime_check=is_prime(i)
    if(is_prime_check):
        primes_list+=[i]
print(primes_list)
