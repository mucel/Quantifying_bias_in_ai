#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:24:22 2024

@author: RalfsArvids123
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import json

# Loading the model from Hugging Face 
model_name = "bigscience/bloom"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name) 


# function for reading JSONL file 
def read_jsonl(file_path): 
    with open(file_path, "r", encoding="utf-8") as file: 
        lines = file.readlines()
        return [json.loads(line) for line in lines]

# function to send prompt to model for yes/no answer
def get_response(prompt):
    modified_prompt = prompt + "\nAnswer with 'yes' or 'no':"
    inputs = tokenizer(modified_prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # extracting the answer 
    if "yes" in response.lower():
        return 1 
    # the default will be no
    else: return 0 

# reading the prompts ss
data = read_jsonl("explicit_output.jsonl")

# processing the prompts for answers
for item in data:
    prompt = item["filled_template"]
    response = get_response(prompt)
    item["decision"] = response  # Add decision directly to the item

# saving the modified data back to the same file (Overwrites the existing file)
with open("explicit_output.jsonl", 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print("Decisions have been added to 'explicit_output.jsonl'.")
