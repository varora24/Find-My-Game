#!/usr/bin/env python3

import os
import sys
import requests
import json
from pprint import pprint
from count_sort import count_sort_func
from bubble_sort import bubble_sort_func

file_name = "games.json"
index = 'Minplayers'
def main():
    response = open(file_name,)# accepts response from json file on github which contains information about all games
    data = json.load(response);
    maxval = 1
    for i in data:
       if i[index] > maxval:
          maxval = i[index]
    data = bubble_sort_func(data,index)
    #data = count_sort_func(data,maxval,index)
    #pprint (sorted(data, key = lambda i: i['Minplayers']))
    #pprint(data)

if __name__ == '__main__':
	main()

