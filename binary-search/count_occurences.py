def count_occuerences(n, x, arr):
    def find_lower_index(n, x, arr):
        low = 0
        high = n - 1
        
        idx = -1
        while low <= high:
            middle = (low + high) // 2
            if arr[middle] < x:
                idx = middle
                low = middle + 1
            
            else:
                high = middle - 1
        
        return idx
    def find_higher_index(n, x, arr):
        low = 0
        high = n - 1
        
        idx = -1
        while low <= high:
            middle = (low + high) // 2
            if arr[middle] <= x:
                idx = middle
                low = middle + 1
            
            else:
                high = middle - 1
        
        return idx        
    print(find_higher_index(n, x, arr) - find_lower_index(n, x, arr))
    
    


count_occuerences(12, 6, [1,4,6,6,6,6,6,7,9,14])