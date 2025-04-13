def mergeSort (unsortedList):
    if len(unsortedList) ==1:
        return unsortedList
    
    midPoint = int(len(unsortedList)/2)
    # i dont' remember this syntax
    firstHalf = unsortedList[:midPoint]
    secondHalf = unsortedList[midPoint:]

    halfA = mergeSort(firstHalf)
    halfB = mergeSort(secondHalf)

    return merge(halfA,halfB)

def merge(first,second):
    i = j = 0
    mergedList = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            mergedList.append(first[i])
            i +=1
        else:
            mergedList.append(second[j])
            j +=1

    while i <len(first):
        mergedList.append(first[i])
        i += 1
    while j <len(second):
        mergedList.append(second[j])
        j +=1
    return mergedList
