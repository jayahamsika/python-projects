# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.
# e.g.

# name1 = "jaya"
# name2 = "James"
# T occurs 0 times

# R occurs 0 times

# U occurs 0 times

# E occurs 1 times

# Total = 1

# L occurs 0 time

# O occurs 0 times

# V occurs 0 times

# E occurs 1 times

# Total = 1

# Love Score = 11

# Print: "Your score is 11."

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50) :
   print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")