# Sets are collection of unordered unique elements
Set1={"pop","rock","soul","hard rock","rock","R&B","rock","disco"}

# Typecasting
album_list = ["Michael Jackson","Thriller","Thriller", 1982] 
album_set = set(album_list)
print("Typecasting: ",(album_set))

# Set operations: Add
album_set.add("NSYNC")
print("Set operations: Add: ",(album_set))

# Set operations: Remove
album_set.remove("NSYNC")
print("Set operations: Remove: ",(album_set))

# Set operations: Verify
print("Set operations: Verify: ",("NSYNC" in album_set))

# Set operations: &
album_set_1 = {"AC/DC","Back in Black", "Thriller"}
album_set_2 = {"AC/DC","Back in Black", "The Dark Side of the Moon"}
#album_set_3 = album_set_1 & album_set_2
album_set_3 = album_set_1.intersection(album_set_2)
print("Set operations: &/intersection: ",(album_set_3))

# Set operations: difference
print("Set operations: difference: ",(album_set_1.difference(album_set_2)))
print("Set operations: difference: ",(album_set_2.difference(album_set_1)))

# Set operations: Union
album_set_4 = album_set_1.union(album_set_2)
print("Set operations: Union: ",(album_set_4))

# Set operations: issubset
print("Set operations: issubset: ", (album_set_1.issubset(album_set_4)))

# Set operations: issuperset
print("Set operations: issuperset: ", (album_set_1.issuperset(album_set_4)))