# for loops

squares=["red","yellow","green","purple","blue"]

for i in range(0,5):
    squares[i] = "white"

print(squares)

# for loops, emunerate
squares1 = ["red","yellow","green"]

for i, square in enumerate(squares1): # square is name
    print(i,square) # same name with the name you created

#
A = [3,4,5]  

for a in A:
    print(a)

#
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])
