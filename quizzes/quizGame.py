# Python quiz game

questions = ("How many elements are in the periodic table? ", 
            "Which animal lays the largest eggs? ",
            "What is the most abundant gas in Earth's atmostphere? ",
            "How many bones are in the human body? ",
            "Which planet in the solar system is the hottest? ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 205"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
i = 0
guesses = []
score = 0

for question in questions:
    print(f"-----[ ANSWER THE QUESTION {i+1}]-----")
    print(question)
    for option in options[i]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[i]:
        score = score + 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct option is: {answers[i]}")
    i = i+1
    print()

score = (score/(i))*100
print("**************************************")
print(f"***      YOUR SCORE IS {score}%.      ***")
print("**************************************")
# print(f"Your Score is {score}%.")

