plans = ["1 month plan" , "2 months plan" , "3 months plan" , "4 months plan" , "6 months plan"]

price = [120 , 190 , 290 , 550 , 720]

details = input("Enter your mobile number -")

print("Your recharge plan is due \n Please select a recharge plan")
selection = input("Enter your favorite plan - ")
prices = price[plans.index(selection)]
total = prices
gst = total*18/100
print("GST(18%)" , gst)
final = total+gst      
print("your total bill is " , final)      
