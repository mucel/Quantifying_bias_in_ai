#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:00:40 2024

@author: RalfsArvids123
"""

import json
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

# Loading the RoBERTa-base model for question answering
model_name = "deepset/roberta-base-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Function for reading JSONL file
def read_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return [json.loads(line) for line in lines]

# Function to get answer (modified)
def get_yes_or_no_answer(context, question):
    inputs = tokenizer(question, context, add_special_tokens=True, return_tensors="pt")
    outputs = model(**inputs)
    
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits)
    
    if answer_start <= answer_end:
        answer = tokenizer.decode(inputs.input_ids[0][answer_start:answer_end + 1])
    else:
        answer = ""
    
    return answer.lower().strip()

# Read the prompts and context
data = read_jsonl("prompts/english/shortened_length/explicit_shortened_english.jsonl")

# Process the prompts for answers
for item in data:
    text = item["filled_template"]
    sentences = text.split(".")
    context = ".".join(sentences[:-1])
    question = "only answer with yes or no: " + sentences[-1].strip()
    
    # Get the answer before saving it
    answer = get_yes_or_no_answer(context, question)  
    
    item["context"] = context
    item["question"] = question
    item["answers"] = answer  

# Save the modified data back to the same file
with open("output/exp_eng_short.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write("\n")

print("Answers have been added to 'output/exp_eng_short.jsonl'.")
