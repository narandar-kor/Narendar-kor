hours = float(input("Enter hours worked : "))
hours_rate = float(input("Enter hour rate : "))

if hours <= 40:
    print("The total pay is : ",hours*hours_rate)
else:
    total_pay = 40*hours_rate+((hours-40)*(hours_rate+(hours_rate/2)))

print("The toatl pay is : ",total_pay)
