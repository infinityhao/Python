# Create file object
File1 = open("C:/Users/V/source/repos/files_write/Example2.txt",'w')

# Using with statement to write a file (auto closed)
with open("C:/Users/V/source/repos/files_write/Example2.txt",'w')as File1:
    File1.write("This is line A\n")
    File1.write("This is line B\n")

# Using with statement to verify on the written file   
with open("C:/Users/V/source/repos/files_write/Example2.txt",'r')as testFile1:    
    print(testFile1.read())

# Alternative way to write a file
Lines = ["This is line 1\n","This is line 2\n","This is line 3\n"]
with open("C:/Users/V/source/repos/files_write/Example2.txt",'w')as File1:
    for line in Lines:
        File1.write(line)

# Using with statement to verify on the written file   
with open("C:/Users/V/source/repos/files_write/Example2.txt",'r')as testFile1:    
    print(testFile1.read())

# Writing file with mode 'a' or append (continue writing)
with open("C:/Users/V/source/repos/files_write/Example2.txt",'a')as File1:
    File1.write("This is line 4\n")

# Using with statement to verify on the written file   
with open("C:/Users/V/source/repos/files_write/Example2.txt",'r')as testFile1:    
    print(testFile1.read())

# Copy and paste to new file
with open("C:/Users/V/source/repos/files_write/Example2.txt",'r')as readFile:
    with open("C:/Users/V/source/repos/files_write/Example3.txt",'w')as writeFile:    
        for line in readFile:
            writeFile.write(line)

# Using with statement to verify on the written file   
with open("C:/Users/V/source/repos/files_write/Example3.txt",'r')as testFile1:    
    print(testFile1.read())