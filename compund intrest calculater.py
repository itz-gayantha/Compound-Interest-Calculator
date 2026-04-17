Principle = float(input("Enter the principle amount: "))
while(Principle <= 0):
    print("Principle amount cannot be less than or euqal to 0")
    Principle = float(input("Enter the principle amount: "))

Rate = float(input("Enter the interest rate: "))
while(Rate <= 0):
    print("Rate cannot be less than or equal to 0")
    Rate = float(input("Enter the interest rate: "))

time = int(input("Enter the time in years"))
while(time <= 0): 
    print("Please enter valid time")
    time = int(input("Enter the time in years: "))

balance =Principle * pow(( 1 + (Rate / 100)),time)
print(f"your balance after {time}year/s is ${balance:.2f}")