#!/usr/bin/env python3

def make_list(arr, category, val):
	position = binary_search(arr, category, 0, len(arr), val)
	high = position
	low = position
	
	if(position == -1):
		return

	while(high+1 < len(arr) and arr[high+1][category] == val):
		high += 1
		
	while(low-1 >= 0  and arr[low-1][category] == val):
		low -= 1

	return range(low, high+1)

#Binary Search to find first instance of a value amongst the dictionary values
def binary_search(arr, category, low, high, val):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle return the position
        if arr[mid][category] == val:
            return mid
 
        # Check subarray from left of the midpoint for value
        elif arr[mid][category] > val:
            return binary_search(arr, category, low, mid - 1, val)
 
        # Check subarray from right of the midpoint for value
        else:
            return binary_search(arr, category, mid + 1, high, val)
 
    else:
        # Element is not present in the array
        return -1
