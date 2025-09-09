def is_anagram(str1,str2):
    length1=len(str1)
    length2=len(str2)
    if(length1==length2):
        for i in str1:
            if(i not in str2):
                return False
        return True
    else:
        return False

s1=input("Enter the first String : ")
s2=input("Enter the second string : ")
print(is_anagram(s1,s2))