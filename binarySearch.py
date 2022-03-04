# Python Program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = int(l + (r - l)/2)
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Test array 
#arr = ["about", "above", "abuse", "actor", "alike", "array", "board", "clean", "buyer", "daily", "crown", "dance", "death", "dealt", "found", "fraud", "globe", "glass", "given", "power", "press", "prove", "quiet", "quick", "queen", "stock", "steel", "stuff", "wrote", "women", "worse", "white"]
#x = "above"

#result = binarySearch(arr, 0, len(arr)-1, x) 
  
