dict_a=eval(input("Enter names,attendence dictionary : "))
defaulters=[]
dict_keys=dict_a.keys()
for i in dict_keys:
    if(dict_a[i]<75):
        defaulters+=[i]
print(defaulters)