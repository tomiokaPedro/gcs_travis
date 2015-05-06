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
