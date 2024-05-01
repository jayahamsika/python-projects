#This code uses for loop to find the average height.

#input heights
students_height = input("Enter heights separated by space:\n").split()

for n in range(0,len(students_height)):
    students_height[n] = int(students_height[n])

#average = sum of items/no.of items

#sum of items
total_height = 0
for height in students_height:
    total_height += height
print(f"total height = {total_height}")

#no. of items
number_of_students = len(students_height)
print(f"number of students = {number_of_students}")

#average calculation
average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")