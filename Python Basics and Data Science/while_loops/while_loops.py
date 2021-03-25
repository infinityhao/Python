# while loops to collect orange square
squares = ["orange","orange","purple","blue"]

Newsquares=[]
i = 0 # start the index at zero

while(squares[i]=="orange"):
    Newsquares.append(squares[i])
    i = i + 1
    
print(Newsquares)

#
x = 3
y = 1

while(y!=x):
    print(y)
    y = y + 1 

#
PlayListRatings = [10,9.5,10,8,7.5,5,10,10]
i = 0

Rating = PlayListRatings[i]

while(Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1