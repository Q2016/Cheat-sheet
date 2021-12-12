// Binary search
        def binary_search_recursive(array, element, start, end):
            if start > end:
                return -1

            mid = (start + end) // 2
            if element == array[mid]:
                return mid

            if element < array[mid]:
                return binary_search_recursive(array, element, start, mid-1)
            else:
                return binary_search_recursive(array, element, mid+1, end)
                
                
//MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)                
