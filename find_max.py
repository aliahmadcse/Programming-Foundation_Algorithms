items = [4, 5, 6, 13, 34, 55, 66, 23, 88, 90]

# finding the max element recursively


def find_max(items):
    # breaking condition
    if len(items) == 1:
        return items[0]
    # get the first value and operate the function to operate on
    # rest of the list
    op1 = items[0]
    print(op1)
    op2 = find_max(items[1:])
    print(op2)

    # performing comparison
    if (op1 > op2):
        return op1
    else:
        return op2

print(find_max(items))
