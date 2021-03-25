# A dictinary has immutable keys to index values
D ={"Key1":1,"Key2":"2", "Key3":[3,3,3], "Key4":(4,4,4),"Key5":5}
print("Key4 = ", D["Key4"])

# Create dictionary
DICT ={"Thriller":"1982","Back in Black":"1980", "The Darkside of the Moon":"1973", "The Bodyguard":"1992"}

# Look up the value
print("\nBack in Black: ",(DICT["Back in Black"]))

# Add new entry 
DICT["Graduation"] = "2007"
print(DICT)

# Del entry
del(DICT["Graduation"])
print(DICT)

# Verify entry
print("\nVerify entry: 'The BodyGuard' in DICT: ", ("The Bodyguard" in DICT))

# List keys/values
print("\nList all the keys: ", DICT.keys())
print("List all the values: ", DICT.values())


