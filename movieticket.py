print("-------------------------------Welcome to the website-------------------------------")

categories = ["silver", "gold", "platinum"]
prices = [150, 250, 400]

print("Categories:", categories)

cat1 = input("Enter first category: ")
cat2 = input("Enter second category: ")

qty1 = int(input("Enter number of tickets for " + cat1 + ": "))
qty2 = int(input("Enter number of tickets for " + cat2 + ": "))

price1 = prices[categories.index(cat1)]
price2 = prices[categories.index(cat2)]

total = (price1 * qty1) + (price2 * qty2)

gst = total * 12 / 100
final_bill = total + gst

print("\n----- FINAL BILL -----")
print(cat1, ":", qty1, "x", price1, "=", price1 * qty1)
print(cat2, ":", qty2, "x", price2, "=", price2 * qty2)
print("Total =", total)
print("GST (12%) =", gst)
print("Your total Bill is ;", final_bill)
print("------------------------Thank you visit again------------------------")