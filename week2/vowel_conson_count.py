s=input("Enter the sentence : ").lower()
vowel_list=["a","e","i","o","u"]
vcount=0
ccount=0
for i in s:
    if(i in vowel_list):
        vcount=vcount+1
    else:
        ccount=ccount+1
print("Vowels="+str(vcount)+" Consonants="+str(ccount))
