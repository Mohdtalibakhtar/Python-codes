sum=0
while True:
    print("Enter the price of item")
    item= input()
    if (item!='q'):
        sum= sum+int(item)
        print(f"Your total bill is {sum}\nIf you want to add item enter price and 'q' if you're done")
    else:
        print("Total bill:",sum)
        print("Thanks for shopping")
        break