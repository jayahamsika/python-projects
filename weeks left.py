# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left.

age = input()
weeks_spent = int(age) * 52
weeks_left = 4680 - int(weeks_spent)
print(f"You have {weeks_left} weeks left.")