questions = ("How many days are there in a week?",
             "How many bones are there in a human body?",
             "If today is Sunday, what day it is tomorrow?",
             "What is (10 + 2) * 10 equal to?",
             "What is the molecular formula for Sodium Chloride?")

options = (("A. 7", "B. 8", "C. 6", "D. 5"),
           ("A. 205", "B. 206", "C. 208", "D. 211"),
           ("A. Friday", "B. Saturday", "C. Monday", "D. Wednesday"),
           ("A. 120", "B. 78", "C. 1200", "D. 12"),
           ("A. SoCh", "B. SdCl", "C. NaCh", "D. NaCl"))

answers = ("A", "B", "C", "A", "D")

score = 0
guesses = []
question_number = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    answer = input("Enter (A, B, C, D): ").upper()

    if answers[question_number] == answer:
        print("You are CORRECT!")
        score += 1
    else:
        print("You are INCORRECT!")

    print()
    question_number += 1

print()
print("------------------")
print(f"Total Score:{score}")

