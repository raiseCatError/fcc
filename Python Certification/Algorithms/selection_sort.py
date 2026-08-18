def selection_sort(array):
    
    n = len(array)

    for x in range(n):
        min_index = x

        for y in range(x + 1, n):

            if array[y] < array[min_index]:
                min_index = y

        if min_index != x:
            array[x], array[min_index] = array[min_index], array[x]
    
    return array    




selection_sort([33, 1, 89, 2, 67, 245])