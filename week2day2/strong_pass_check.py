import string

def check_strength(password1):
    length=len(password1)
    haslower=False
    hasdigit=False
    hasSpec=False
    hasupper=False
    special_chars=string.punctuation
    if(length>=8):
        for i in password1:
            if(i.islower()):
                haslower=True
            if(i.isupper()):
                hasupper=True
            if(i.isdigit()):
                hasdigit=True
            if(i in special_chars):
                hasSpec=True
    else:
        return False
    if(hasdigit and haslower and hasupper and hasSpec):
        return True
    else:
        return False
p1=input("Enter your Password : ")
strong_pass=check_strength(p1)
if(strong_pass):
    print("Strong Password")
else:
    print("Weak Password")