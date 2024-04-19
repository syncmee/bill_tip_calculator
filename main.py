#Bill & Tip Calculator
#Write your code below this line 👇

print("Welcome to the Bill & Tip Calculator")
total_bill = input("How much was the total bill?\n\u20B9")
tip = input("How much do you want to tip?\n")
total_people = input("How many people to split the bill with?\n")
tb = int(total_bill)
tip1 = int(tip)
tp = int(total_people)
#Each Person Should Pay 👇
#total_bill + tip / total_people
Final_Split = (tb + tip1) / tp
print(f"Each person should pay:\u20B9{Final_Split}")

#test
