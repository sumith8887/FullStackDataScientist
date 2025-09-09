import math

def math_calulation(func,val):
    if(func=="sqrt"):
        print(math.sqrt(val))
    elif(func=="factorial"):
        print(math.factorial(val))
    elif(func=="sin"):
        print(math.sin(val))
    elif(func=="cos"):
        print(math.cos(val))
    else:
        print("Invalid math function")

while True:
    s=input("Enter your math statement : ").split("(")
    if(s[0]=="exit"):
        break
    func=s[0].lower()
    r=s[1].split(")")
    val=int(r[0])
    math_calulation(func,val)
