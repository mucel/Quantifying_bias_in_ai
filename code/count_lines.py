#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:05:50 2024

@author: RalfsArvids123
"""

# Open the JSONL file in read mode
with open('output/imp_lv.jsonl', 'r') as file:
    # Count the number of lines in the file
    line_count = sum(1 for line in file)

# Print the total number of lines
print("Total number of lines:", line_count)
