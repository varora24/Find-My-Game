#!/usr/bin/env python3

import os
import sys
import requests
import json
from pprint import pprint
from count_sort import count_sort_func
from bubble_sort import bubble_sort_func
from binary_search import *
from filter_list import *

file_name = "games.json"
index = 'Maxplayers'
index2 = 'Category'
dict_index = {'Category': 'Strategy', 'Format': 'Website'}

def main():
    response = open(file_name,)# accepts response from json file on github which contains information about all games
    data = json.load(response);
    maxval = 1
    for i in data:
       if i[index] > maxval:
          maxval = i[index]
    data = bubble_sort_func(data,index)
    found = make_list(data,index,3)
    found2 = filter_list(found, index2, "Strategy")
    found3 = filter_list_dict(found, dict_index)
    print(f'{found}\n\n\n{found2}\n\n\n{found3}')
	
    #data = count_sort_func(data,maxval,index)`
 
if __name__ == '__main__':
	main()

