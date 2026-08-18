def quick_sort(array):

    if len(array) <= 0:
        return array
    else:
        pivot_value = len(array) // 2
    
    lt_pivot = []
    et_pivot = []
    gt_pivot = []

    for x in array:
        if array[pivot_value] > x:
            lt_pivot.append(x)
        if array[pivot_value] == x:
            et_pivot.append(x)
        if array[pivot_value] < x:
            gt_pivot.append(x)
    
    sorter = lt_pivot + et_pivot + gt_pivot

      
    print('LT:',lt_pivot)
    print('ET:',et_pivot)
    print('GT:',gt_pivot)

    print('Sorted:',sorter)

    return quick_sort(lt_pivot) + et_pivot + quick_sort(gt_pivot)
  
    

quick_sort([83, 4, 24, 2])

