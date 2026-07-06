print("-------------------------------Welcome to the website-------------------------------")

categories = ["silver", "gold", "platinum"]
prices = [100, 200, 400]

cat1 = input("Enter the first category - ")
cat2 = input("Enter the second category - ")

quantity1 = int(input("Enter the number of tickets for category " + cat1 + "-"))
quantity2 = int(input("Enter the number of tickets for category " + cat2 + "-"))

price1 = prices[categories.index(cat1)]
price2 = prices[categories.index(cat2)]
total = price1*quantity1 + price2*quantity2
cate1 = price1*quantity1
cate2 = price2*quantity2
print("Your" , cat1 , "total is" , cate1)
print("Your" , cat2 , "total is" , cate2)
print("Your sub-total amount is -" , total)
gst = total*12/100
print("GST(12%)- " , gst )
final = total + gst
print("Your total bill is" , final)
print("--------------------------------Thank you visit Again-------------------------------")
