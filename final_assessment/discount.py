def calcluate_price(items):
    if(not isinstance(items,dict)):
        print("Invalid input of data provided")
        return
    if(len(items)==0):
        print("No items are present in the cart")
        return
    else:
        count=len(items)
        price=sum(items.values())
        if(count>5):
            discount=price*0.1
            print("Total Price: ",(price-discount))
        else:
            print("Total Price: ",price)
try:
    items=eval(input("Enter the cart items in form of item:price(key:value pairs) : "))
    calcluate_price(items)
except Exception as e:
    print("Invalid input format. Please enter a valid dictionary. Error:", e)