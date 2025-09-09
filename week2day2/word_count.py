def word_frequency(list_a):
    dict_a={}
    for i in list_a:
        dict_a[i]=list_a.count(i)
    return dict_a

s=list(map(str,input("Enter the Sentence : ").split()))
print(word_frequency(s))