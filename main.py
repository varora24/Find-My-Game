#!/usr/bin/env python3

import os
import sys
import requests
import json
from pprint import pprint
from count_sort import count_sort_func
from bubble_sort import bubble_sort_func
from binary_search import binary_search
from binary_search import make_list
from filter_list import filter_list
file_name = "games.json"
index = 'Minplayers'
index2 = 'Category'
def main():
    response = open(file_name,)# accepts response from json file on github which contains information about all games
    data = json.load(response);
    maxval = 1
    for i in data:
       if i[index] > maxval:
          maxval = i[index]
    data = bubble_sort_func(data,index)
    found = make_list(data,index, 3)
    found2 = filter_list(found, index2, "Strategy")
    print(f'{found}\n\n\n{found2}')
	
    #data = count_sort_func(data,maxval,index)`
 
if __name__ == '__main__':
	main()

