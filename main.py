import os
import sys
import requests
import json
import pprint
from quick_sort import quick_sort_func #allows us to call the quick_sort python code


URL = "https://raw.githubusercontent.com/varora24/Find-My-Game/data/games.json"



def main():
	response = requests.get(URL).json(); # accepts response from json file on github which contains information about all games
	response_sorted = quick_sort_func(response,1,2,False)

	pprint.pprint(response_sorted)


if __name__ == '__main__':
	main()

