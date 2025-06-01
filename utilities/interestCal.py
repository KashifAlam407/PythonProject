#####  Compound Interest Calculator  #######
###111111111111111111111111111111111111111
### This program will not work for 0 input. 
amount = 0
rate = 0
time = 0

while amount <= 0:
    amount = int(input("Enter the Principal amount: "))
    if amount <= 0:
        print("Principal amount Invalid!")

while rate <= 0:
    rate = int(input("Enter the rate: "))
    if rate <= 0:
        print("Rate Invalid!")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time Invalid!")

print(f"Simple Insterest is: {(amount*rate*time)/100} ")

total = amount*pow((1+rate/100), time)  ## here pow(base, power)
print(f"Compound Interest is: {total:.2f}") ## here total:.2f is format specifier (takes upto 2 decimal places)   


###222222222222222222222222222222222222222
### This program will work for 0 input.

amount = 0
rate = 0
time = 0

while True:
    amount = float(input("Enter the Principal amount: "))
    if amount < 0:
        print("Principal amount Invalid!")
    else:
        break

while True:
    rate = float(input("Enter the rate: "))
    if rate < 0:
        print("Rate Invalid!")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time Invalid!")
    else:
        break

print(f"Simple Insterest is: {(amount*rate*time)/100} ")

total = amount*pow((1+rate/100), time)  ## here pow(base, power)
print(f"Compound Interest is: {total:.2f}") ## here total:.2f is format specifier (takes upto 2 decimal places) 
