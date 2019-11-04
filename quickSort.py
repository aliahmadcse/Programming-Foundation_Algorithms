# dataset for sorting
items = [2, 6, 8, 53, 56, 23, 87, 41, 49, 19]


def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)
        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(dataValues, first, last):
    #choosing the first item as the first value
    pivotValue=dataValues[first]
    #establishing the upper and lower indexes
    lower=first+1
    upper=last

    #started searching for crossing point
    done=False
    while not done:
        #advance the lower index
        while lower<=upper and dataValues[lower]<=pivotValue:
            lower+=1
        #advance the lower index
        while upper>=lower and dataValues[upper]>=pivotValue:
            upper-=1
        #if the two indexes crosses, we find the split point
        if upper<lower:
            done=True
        else:
            temp=dataValues[lower]
            dataValues[lower]=dataValues[upper]
            dataValues[upper]=temp
    
    #when the split point is found, exchange the pivot value
    temp=dataValues[first]
    dataValues[first]=dataValues[upper]
    dataValues[upper]=temp
    #return the split point index
    return upper         


#testing
print(items)
quickSort(items,0,len(items)-1)
print(items)