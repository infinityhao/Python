# Python knows to start a new line
# Create file object
File1 = open("C:/Users/V/Desktop/Loss Credit card.txt",'r')

# Use the file object to obtain information
print("The File1.name is: " ,File1.name)

print("The File1.mode is: " ,File1.mode)

# Use the with statement to open and close file object (auto closed)
with open("C:/Users/V/Desktop/Loss Credit card.txt",'r')as File1:
    file_stuff = File1.read()
    print(file_stuff)
    # File1.closed
    
print("File1.closed is: ", File1.closed)

# Use the readline() method instead of read()
with open("C:/Users/V/Desktop/Loss Credit card.txt",'r')as File1:
    file_stuff = File1.readline(16) # read first line 16 characters
    print(file_stuff)
    file_stuff = File1.readline(5) # read second line 5 characters
    print(file_stuff)
    file_stuff = File1.readline(9) # read third line 9 characters
    print(file_stuff)
        
print("File1.closed is: ", File1.closed)

# Iterate through the lines

with open("C:/Users/V/Desktop/Loss Credit card.txt","r") as File1:
        i = 0;
        for line in File1:
            print("Iteration", str(i), ": ", line)
            i = i + 1;
File1.closed

# Read all lines and save as a list

with open("C:/Users/V/Desktop/Loss Credit card.txt","r") as File1:
    FileasList = File1.readlines()
    
# Print the lines
print("FileasList[0] = ", FileasList[0])
print("FileasList[1] = ", FileasList[1])
print("FileasList[2] = ", FileasList[2])
