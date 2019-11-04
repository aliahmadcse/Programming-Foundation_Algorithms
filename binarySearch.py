items=[2,13,16,33,55,67,77,78,89,90]

def binarySearch(item,itemList):
    #get the list size
    listSize=len(itemList)-1
    #set the lower and upper index
    lowerIdx=0
    upperIdx=listSize

    while lowerIdx<=upperIdx:
        #calculating the middle point
        mid = (lowerIdx+upperIdx)//2
        #if the item is found, return its index
        if (item==itemList[mid]):
            return mid
        #otherwise calculate the next mid
        elif itemList[mid]<item:
            lowerIdx=mid+1
        else:
            upperIdx=mid-1
    #if nothing found, return none
    if lowerIdx>upperIdx:
        return None

#testing 
print(binarySearch(15,items))
print(binarySearch(16,items))
