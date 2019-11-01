# create a hash table all at once
item1 = dict({"key1": 1, "key2": 2, "key3": "three"})

# create a hash table progressively
item2 = {}
item2["key1"] = 1
item2["key2"] = 2
item2["key3"] = 3
print(item2)

# get an invalid key
print(item2.get("key6", 6))

# replace an item
item2["key2"] = "two"
print(item2)

# iterate over the hash table
for key, value in item2.items():
    print(f"{key},{value}")
