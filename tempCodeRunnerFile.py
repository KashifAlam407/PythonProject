import random

r = random.randint(1, 100)
i = 1
print("Enter a number between 1 and 100: ")
while (i<100):
    num = int(input())
    if num>r:
        print(f"Guess number less than {num}")
    elif num<r:
        print(f"Guess number bigger than {num}")
    else:
        print("Congratulations! You have guesse a right number.")
        break
    i += 1

score =  100/i
print("----------------------------")
print(f"-----Your Score is: {score}-----")
print("----------------------------")

