# Pre-defined functions
album_ratings = [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5]

print("Len: ", len(album_ratings))

print("Sum: ", sum(album_ratings))

print("Sorted: ", sorted(album_ratings))
#print("Sort: ", album_ratings.sort())

album_ratings.reverse()
print("Reverse: ", album_ratings)

# Making functions
def add1(a): # def descriptive of what it does
    b = a + 1
    return b

print("add1(5): ", add1(5))

# Multiple parameters
def mult(a,b):
    c=a*b
    return c

print('mult(2,"Michael Jackson "): ', mult(2,"Michael Jackson "))

# void functions
def mj():
    print("Michael Jackson")

print("Void functions: ", mj())

# printStuff function
Stuff = [10.0,8.5,9.5]

def printStuff(Stuff):
    for i, s in enumerate(Stuff):
        print("Album", i, "Rating is ", s)

printStuff(Stuff)

# Collecting arguments
def ArtistNames(*names): # depends on input quantity
    for name in names:
        print(name)

ArtistNames("Jackie Cheong", "Alan Tam", "Michael Jackson")

# Global scope: if local variable is not defined, python will check the global scope variable
def PinkFloyd():
    global ClaimedSales
    ClaimedSales = "45 millions"
    return ClaimedSales

PinkFloyd()
print("ClaimedSales: ", ClaimedSales)
