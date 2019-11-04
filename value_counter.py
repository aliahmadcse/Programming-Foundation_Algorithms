# using a hash table to count individual item

# define a set of items that we wanna count
items = ['apple', 'pear', 'orange', 'banana', 'apple', 'orange', 'apple',
         'pear', 'banana', 'orange', 'apple', 'kiwi', 'pear', 'apple', 'orange']

# creating a hash table
counter = dict()
# looping over each item in list
for item in items:
    counter[item] = counter.get(item, 0)+1

print(counter)
