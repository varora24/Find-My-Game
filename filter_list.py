#!/usr/bin/env python3

#Filters a given list based on a given category and value
def filter_list(arr, category, val):
	new_arr = []	

	for i in range(0, len(arr)):
		if(arr[i][category] == val):
			new_arr.append(arr[i])

	return new_arr

#Same function as filter_list but uses a dictionary with category and
#val pairs to test more than one parameter
def filter_list_dict(arr, categories):
	new_arr	= []

	for i in range(0, len(arr)):
		found = True
		for category in categories:
			if(arr[i][category] != categories[category]):
				found = False
				continue

		if(found):
			new_arr.append(arr[i])

	return new_arr
