dict_a=eval(input("Enter items with prices : "))
bill=0
for i in dict_a.keys():
    bill+=dict_a[i]
print(bill)