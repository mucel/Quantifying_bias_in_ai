#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:00:33 2024

@author: RalfsArvids123
"""

import json

def shorten_jsonl(input_file, output_file, max_lines=100):
    """Shortens a JSONL file to a specified number of lines.

    Args:
        input_file (str): Path to the input JSONL file.
        output_file (str): Path to the output JSONL file.
        max_lines (int, optional): Maximum number of lines to keep. Defaults to 100.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile:

        for i, line in enumerate(infile):
            if i >= max_lines:  # Stop after max_lines
                break
            json.dump(json.loads(line), outfile) 
            outfile.write('\n')


# Use the function
shorten_jsonl("implicit.jsonl", "implicit_shortened.jsonl", 100)
print("Created 'explicit_output_shortened.jsonl' with the first 100 lines.")
