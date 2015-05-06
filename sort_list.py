def sort_list(array):

    unsorted_array = array
    array_size = len(unsorted_array)


    for i in range(array_size -1, 0, -1):
        
        j = 0

        while j<i:

            if(unsorted_array[j]>unsorted_array[j+1]):
                aux = unsorted_array[j]
                unsorted_array[j] = unsorted_array[j+1]
                unsorted_array[j+1] = aux
            
            j+=1

    return unsorted_array

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist