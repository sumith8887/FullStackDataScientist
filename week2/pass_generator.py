import random

def password_generator(length):
    characters="~!@#$%^&*()_+`1234567890-=QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?/.,mnbvcxzasdfghjkl;poiuytrewq"
    password=""
    for i in range(length):
        password=password+random.choice(characters)
    return password

length=int(input("Enter the length for your pass : "))
print(password_generator(length))