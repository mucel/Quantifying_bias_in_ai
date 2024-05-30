#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:00:40 2024

@author: RalfsArvids123
"""

from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import json

# Loading the RoBERTa-base model for question answering
model_name = "deepset/roberta-base-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

def read_jsonl(file_path): 
    with open(file_path, "r", encoding="utf-8") as file: 
        lines = file.readlines()
        return [json.loads(line) for line in lines]

# Function to get answer using RoBERTa
def get_answer(question, context):
    inputs = tokenizer(question, context, add_special_tokens=True, return_tensors="pt")
    outputs = model(**inputs)

    answer_start = outputs.start_logits.argmax()
    answer_end = outputs.end_logits.argmax() + 1  # Inclusive

    answer = tokenizer.decode(inputs.input_ids[0][answer_start:answer_end])
    return answer

# Read the prompts and context (assuming your JSONL has "question" and "context" fields)
data = read_jsonl("explicit_output_shortened.jsonl")

# Process the prompts for answers
for item in data:
    question = item["question"] 
    context = item["context"] 
    answer = get_answer(question, context)
    item["answer"] = answer  # Add answer to the item

# Save the modified data back to the same file
with open("explicit_output_shortened.jsonl", 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print("Answers have been added to 'explicit_output.jsonl'.")
