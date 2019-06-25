#sequential or linear search (search an object in a list or iterable:cursor)
def seq_search(l, elem):
    for index,item in enumerate(l):
        if elem==item:
            return index
    return -1         #otherwise
   

#binary search (element in list is in order a2z, iterable does not work here because it needs a length)
def bin_search(items, elem):
    start, end = 0, len(items) - 1 #index in a iterable
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


"""
Binary Search requires O(log N) steps where N is the size of the search space. 
But linear search needs O(N) steps in the worst case, 
but doesn't require the data to be sorted, or the function to be monotonous
"""
