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

#Function that would filter through a list of dictionaries to see if they had integer values.
#If so the data would go through a bubble sort and binary search
#All other category and value pairs would be searched for via a for sequential search
#
#def filter_list_all(arr, categories):
#
#	for category in categories:
#		if type(categories[category] == int):
#			arr = bubble_sort_func(arr,category, categories[category])
#			arr = make_list(arr, category, categories[category])
#		else
#			cat_dict[category] = categories[category]
#
#	new_arr = []
#	for i in range(0, len(arr)):
#		found = True
#		for cat in cat_dict:
#			if(arr[i][cat] != cat_dict[cat]):
#				found = False
#				continue
#
#		if found:
#			new_arr.append(arr[i])
#
#	return new_arr
	

	
