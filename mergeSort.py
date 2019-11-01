# implement a merge sort with recursion

items = [6, 20, 8, 19, 56, 23, 7, 56, 34, 10]


def merge_sort(dataset):
    # diving the array into two equal halfs
    if len(dataset) > 1:
        mid = len(dataset)//2
        leftArr = dataset[:mid]
        rightArr = dataset[mid:]
        # recursive calls to furthur split the arrays
        merge_sort(leftArr)
        merge_sort(rightArr)

        # taking variables for merging
        i = 0
        j = 0
        k = 0
        # while both arrays have content
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                dataset[k] = leftArr[i]
                i += 1
            else:
                dataset[k] = rightArr[j]
                j += 1
            k += 1
            
        #if the left array still have values, add them
        while i < len(leftArr):
            dataset[k] = leftArr[i]
            i += 1
            k += 1

        # if the right array still have values, add them
        while j < len(rightArr):
            dataset[k] = rightArr[j]
            j += 1
            k += 1


# testing the algorithm
if __name__=="__main__":
    print(items)
    merge_sort(items)
    print(items)
