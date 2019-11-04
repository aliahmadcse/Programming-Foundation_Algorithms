items1 = [1, 4, 6, 21, 44, 56, 77, 85, 99]
items2 = [1, 4, 6, 21, 16, 56, 77, 85, 99]

# this function return true or false on the basis of list is
# sorted or not
def is_sorted(dataset):
    return all(dataset[i] <= dataset[i+1] for i in range(0, len(dataset)-1))


#testing
print(is_sorted(items1))
print(is_sorted(items2))