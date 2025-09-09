def find_long_word(list_a):
    result=""
    max_leng=len(list_a[0])
    for i in list_a:
        if(len(i)>max_leng):
            result=i
            max_leng=len(i)
    return result

s=input("Enter the sentence : ")
list_s=s.split()
print(find_long_word(list_s))