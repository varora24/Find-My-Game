#!/usr/bin/env python3

#Filters a given list based on a given category and value
def filter_list(arr, category, val):
	new_arr = []	

	for i in range(0, len(arr)):
		print(i)
		if(arr[i][category] == val):
			new_arr.append(arr[i])

	return new_arr	
