import os
import sys


def check_valid(value):
   if not value['Title']:
      value['Title'] = 'No name'
   if not value['Minplayers']:
      value['Minplayers'] = 1
   if not value['Maxplayers']:
      value['Maxplayers'] = 2
   if not value['Category']:
      value['Category'] = 'Fun'
   if not value['Description']:
      value['Description'] = 'No description'
   if not value['Time']:
      value['Time'] = '30 min'
   if not value['Price']:
      value['Price'] = '0'
   if not value['Format']:
      value['Format'] = 'Website'
   if not value['URL']:
      value['URL'] = 'no URL'
   if not value['Picture']:
      value['Picture'] = 'https://i.ibb.co/qxjcPtZ/Untitled-design.png'

   return value


def bubble_sort_func(data,index):
   length = len(data)
   for i in range(length-1):
      data[i] = check_valid(data[i])
      
      for j in range(0,length-i-1):
         if data[j][index] > data[j+1][index]:
            data[j],data[j+1] = data[j+1],data[j]

   return data
