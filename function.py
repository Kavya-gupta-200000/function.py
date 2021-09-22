# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 04:52:18 2021

@author: kcs
"""

input_string = "Mississippi"
frequencies = {}

for char in input_string:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1
        
        #show output
print ("Per frequency in '{}' is :\n {}".format(input_string, str(frequencies)))