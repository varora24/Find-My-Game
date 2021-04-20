#!/usr/bin/env python3

def make_list(arr, category, val):
	position = binary_search(arr, category, 0, len(arr), val)
	high = position;
	low = position;
	
	if(position == -1):
		return

	while(high+1 < len(array) and atoi(arr[high+1][category]) == val):
		high++
		
	while(low-1 >= 0  and atoi(arr[low-1][category]) == val):
		low--

	return range(low, high)

#Binary Search to find first instance of a value amongst the dictionary values
def binary_search(arr, category, low, high, val):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle return the position
        if atoi(arr[mid][category]) == val:
            return mid
 
        # Check subarray from left of the midpoint for value
        elif atoi(arr[mid][category]) > val:
            return binary_search(arr, low, mid - 1, val)
 
        # Check subarray from right of the midpoint for value
        else:
            return binary_search(arr, mid + 1, high, val)
 
    else:
        # Element is not present in the array
        return -1