# Tuples is immutable
# Ratings[0] = '1' x
# Tuples
Ratings = (10,9,6,5,10,8,9,6,2)
tuple1=("disco",10,1.2)
type(tuple1)
print("Tuples is immutable: ", (tuple1[0]))
print("Tuples is immutable: ", (tuple1[-1]))

# Tuples: Concartenate
tuple2 = tuple1 + ("hard rock",10)
print("\nConcartenate: ",(tuple2))

# Tuples: Slicing
print(tuple2[0:3])
print(tuple2[3:5])
print(len((tuple2)))
print("\nThe length of tuple: ", len(("disco", 10, 1.2, "hard rock", 10)))

# Tuples: Sorting 
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

# Tuples: Nesting
NT = (1, 2,("pop", "rock"),(3,4),tuple1)
print("\nNesting tuple NT: ", NT)
print("NT[2][1]: ", NT[2][1])

# Lists: Mutable
L=["Michael Jackson", 10.1, 1982]
L[0] = "Janet Jackson"
print("\nLists: Mutable: ", L[0])
del(L[1])
print("Lists: Mutable: ", L)

# Lists: Slicing
print("\nLists: Slicing: ", L[1:5])

# Lists: Concartenate
L1=L+["pop",10]
print("\nLists: Concartenate: ", L1)

# Lists: Extend
L.extend(["extended"])
print("\nLists: Extend: ", L)

# Lists: Append (add one element)
L.append(["A", "B"])
print("\nL.append = ", L[-1])

# Convert string to list
print("\nConvert string to list: Split" ,"hard rock".split())
print("Convert string to list: Split" , "A,B,C,D".split(","))

# Lists: Clone
LClone = L[:]
L[0]="Michael Jackson"
print("\nLists: Clone: ", LClone) # it will not change

# List: Index
print("\nLists: Index: ", L.index("Michael Jackson"))
print("Lists: Index: ", L[1:4])