# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
print(len(subjects))
for subject in subjects:
    print(subject)
    #print out each subject but stop when you reach "history"
for subject in subjects:
    if subject == "History":
        break
    print(subject)
# skip over "science: and print the rest"
for subject in subjects:
    if subject == "science":
        continue 
    print(subject)

# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for index in range(len(subjects)):
    print("subject" + str(index) + ": " + subjects[index])

# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
total = 0 
for number in numbers:        
    total += number    #+= means it just adds on the number to the previous total 
print(total)

new_numbers = list(range(1,600001))
#this creates a list of numebrs from 1-60
#challenge: sum up all the humbers from 1 to 60 and print the total 
total = 0 
for number in new_numbers: 
    total += number
print(total)

Evins_list = list(range(5,25))
total = 0 
for number in Evins_list:
    total += number 
print(total)