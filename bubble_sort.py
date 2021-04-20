import os
import sys

def bubble_sort_func(data,index):
   length = len(data)

   for i in range(length-1):
      for j in range(0,length-i-1):
         if data[j][index] > data[j+1][index]:
            data[j],data[j+1] = data[j+1],data[j]

   return data
