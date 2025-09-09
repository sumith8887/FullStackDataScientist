list_a=list(map(str,input("Enter Students names : ").split()))
dub_list=[]
for i in list_a:
    if(list_a.count(i)>1):
        dub_list+=[i]
print(set(dub_list))