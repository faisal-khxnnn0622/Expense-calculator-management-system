# Restaurant bill of any two order

menu = ["pizza" , "burger" , "fries" , "nuggets" , "chicken65" , "sandwich"]
pricess = [260 , 200 , 120 , 140 , 130 , 110]

item1 = input("Enter first food item ;")
item2 = input("Enter your second food item ;")

price = pricess[menu.index(item1)]
price1 = pricess[menu.index(item2)]

final = price+price1
print("Sub total :" , final)
gst = final *18/100
print("GST(18%)" , gst)
print("Your total bill is ;" ,final+gst )


#user entered somthng which is not present in the menu

menu = ["pizza" , "burger" , "fries" , "nuggets" , "chicken65" , "sandwich"]
pricess = [260 , 200 , 120 , 140 , 130 , 110]

item1 = input("Enter first food item ;")
item2 = input("Enter your second food item ;")
item3 = input("Enter your third food item :")
price = pricess[menu.index(item1)]
price1 = pricess[menu.index(item2)]
price2 = pricess[menu.index(item3)]
final = price+price1+price2
print("Sub total :" , final)
gst = final *18/100
print("GST(18%)" , gst)
print("Your total bill is ;" ,final+gst )



