def is_palindrome(sentence):
    sentence=sentence.replace(" ","")
    sentence=sentence.lower()
    new_sent=sentence[::-1]
    print(sentence,new_sent)
    if(new_sent==sentence):
        return True
    else:
        return False
s=input()
print(is_palindrome(s))