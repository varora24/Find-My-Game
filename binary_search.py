#!/usr/bin/env python3

#Creates a list for all of the values of a specific category
def make_list(arr, category, val):
	position = binary_search(arr, category, 0, len(arr), val)

	#Checks if an error occured
	if(position == -1):
		return

	#Checks for special players instance of call
	if(category == "Minplayers"):
		return make_list_players(arr, category, val, position)

	high = position
	low = position

	while(high+1 < len(arr) and arr[high+1][category] == val):
		high += 1
		
	while(low-1 >= 0  and arr[low-1][category] == val):
		low -= 1

	return range(low, high+1)

#Make list function for player counts
def make_list_players(arr, category, val, position):
	high = position
	low = position
	pos_arr = [position]

	while(high+1 < len(arr) and arr[high+1][category] <= val):
		if(arr[high+1]["Maxplayers"] >= val):
			pos_arr.append(high+1)
		high += 1
		
	while(low-1 >= 0 and arr[low-1][category] <= val):
		if( arr[low-1]["Maxplayers"] >= val):
			pos_arr.insert(0, low-1)
		low -= 1

	return pos_arr

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

