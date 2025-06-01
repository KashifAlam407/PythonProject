## Shopping Cart Programm

foods = []
prices = []
total = 0

while True:
    food = input("Enter the name of Food (q to quit): ")
    if food.lower()=='q':
        break
    else:
        price = float(input(f"Enter the price of {food} Rs: "))

        foods.append(food)
        prices.append(price)
    
print("------ YOUR CART ------")
for food in foods:
    print(food, end=" ")

for price in prices:
    total = total + price
print()   ### 
print(f"Your total is: Rs {total}.")




    
