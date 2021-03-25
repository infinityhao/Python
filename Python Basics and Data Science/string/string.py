# strings are immutable
# Name[0] = 'j' x

Name = "Michael Jackson"
print(Name[0])

# negative index (Last number -1)
print(Name[-1]) 

# slicing
print(Name[0:4])
print(Name[8:12])

# Stride (skip every 2 letters)
print(Name[::2]) 
print(Name[0:5:2]) # slicing from 0-5 letters and get every second element

# tuples: slicing
print(len("Michael Jackson")) # length

# concatenate
print(Name + " is the best")

# tuples
print(3*"Michael Jackson ")

# escape sequences
print("Michael Jackson\n is the best")
print("Michael Jackson\t is the best") # a tab
print("Michael Jackson\\ is the best") # to put backslash
print(r"Michael Jackson is the best")  # r to tell python to display as raw string

# string method
print(Name.upper()) # change all letters yo uppercase
print(Name.replace("Michael", "Janet"))
print(Name.find("el")) # if can't find the result will be -1


