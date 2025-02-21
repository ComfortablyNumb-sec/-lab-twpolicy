# SFS Lab 3 - Python Regex Questions
# EC May, 2022
# Add your answer to each of the questions
import re
file =open("apache_log", "r")
data = file.read()


# Q1 Import the apache log and print out the contents

#print (data)

# once you have answer for Q1 comment out the print statement to keep things tidy

# Q2 Use regex to find any instance of the word notice?

x1 = re.findall ("notice", data)
print (x1)

# Q3 Use regex to find any instance of the word error?
# your code here

x1 = re.findall ("error", data)
print (x1)

# Q4 Use regex to count any instance of the word notice?
# your code here
x = re.search ("notice", data)
print (x)

# Q5 Use regex to count any instance of the word error?
# your code here
x = re.search ("error", data)
print (x)
# Q6 Use regex to count any instance of the letter p?
# your code here
x = re.findall("x", data)
print (x)

# Q7 Use regex to find any instance of the string jk2_init?
# your code here

x = re.findall("jk2_init", data)
print (x)

# Q8 Use regex to find any appearance of the number 6754?
# your code here
pattern = r"6754"
x = re.findall(pattern, data)
print (x)

# Q9 Use regex to find any appearance of the number 6?
# your code here

pattern = r"6"
x = re.findall(pattern, data)
print (x)

# Q10 Use regex to find any ip addresses?
# your code here


x = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", data)
print (x)

# Q11 Create a script that will ask for user input, ask the user to enter a letter, then use regex to return any matches of that letter in the file?
# your code here


text = input("type  in your letter: ")
x = re.findall(text, data)
print (x)

# Q12 adapt your answer from Q11, to use a function to search the file, the function should take one parameter - the letter you are searching for?
# your code here

y = input("type  in your letter: ")
def letter(y):
    x = re.findall(y, data)
    return x

print(letter(y))
    




