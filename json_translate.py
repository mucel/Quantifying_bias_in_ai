#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:59:16 2024

@author: RalfsArvids123
""" 
import json
from google.cloud import translate_v2 as translate

def translate_text(text, target='lv'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)
    return result['translatedText']

def translate_jsonl_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line)
            if 'filled_template' in data:
                original_text = data['filled_template']
                translated_text = translate_text(original_text)
                data['filled_template'] = translated_text
            outfile.write(json.dumps(data, ensure_ascii=False) + '\n')

input_file = '/Users/RalfsArvids123/Downloads/textmining_project/implicit.jsonl'
output_file = '/Users/RalfsArvids123/Downloads/textmining_project/implicit_output.jsonl'
translate_jsonl_file(input_file, output_file)
