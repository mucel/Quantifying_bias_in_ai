#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:00:40 2024

@author: RalfsArvids123
"""


import json

from transformers import AutoModelForQuestionAnswering, AutoTokenizer

# Loading the RoBERTa-base model for question answering
model_name = "deepset/roberta-base-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)


# function for reading JSONL file
def read_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return [json.loads(line) for line in lines]


# Function to get answer (modified)
def get_yes_or_no_answer(text):
    sentences = text.split(".")
    context = ".".join(sentences[:-1])  # Everything before the last sentence
    question = (
        "only answering with yes or no: " + sentences[-1].strip()
    )  # Last sentence

    inputs = tokenizer(
        question, context, add_special_tokens=True, return_tensors="pt"
    )
    outputs = model(**inputs)

    answer_start = outputs.start_logits.argmax()
    answer_end = outputs.end_logits.argmax() + 1  # Inclusive

    answer = tokenizer.decode(inputs.input_ids[0][answer_start:answer_end])
    """
    if "yes" in answer.lower():
        return "yes"
    else:
        return "no"
    """
    return answer


# Read the prompts and context (assuming your JSONL has "text" field)
data = read_jsonl(
    "prompts/english/shortened_length/explicit_shortened_english.jsonl"
)

# Process the prompts for answers
for item in data:
    text = item["filled_template"]
    answer = get_yes_or_no_answer(text)
    item["answers"] = answer  # Add answer to the item

# Save the modified data back to the same file
with open("output/exp_eng_short.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write("\n")

print("Answers have been added to 'explicit_output.jsonl'.")
