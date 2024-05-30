#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:00:40 2024

@author: RalfsArvids123
"""

import json

import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# Loading the RoBERTa-base model for question answering
model_name = "timpal0l/mdeberta-v3-base-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)


# Function for reading JSONL file
def read_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return [json.loads(line) for line in lines]


def get_yes_or_no_answer(context, question):
    inputs = tokenizer(
        question, context, add_special_tokens=True, return_tensors="pt"
    )
    print("Tokenized Inputs:", inputs)

    outputs = model(**inputs)
    print("Model Outputs:", outputs)

    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits)

    if answer_start <= answer_end:
        answer = tokenizer.decode(
            inputs.input_ids[0][answer_start : answer_end + 1]
        )
        print("Raw Answer:", answer)
        if answer in ["<s>", "</s>", "<pad>", ""]:
            return "no answer"
    else:
        answer = ""

    return answer.lower().strip()


def get_answer(context, question):
    qa_model = pipeline("question-answering", model_name)
    QA_input = {"question": question, "context": context}
    return qa_model(question=question, context=context)["answer"]


# Read the prompts and context
data = read_jsonl(
    "prompts/english/shortened_length/explicit_shortened_english.jsonl"
)

# Process the prompts for answers
for item in data:
    text = item["filled_template"]
    sentences = text.split(".")
    context = ".".join(sentences[:-1])
    question = "Only answering with yes or no, " + sentences[-1].strip()

    # Get the answer before saving it
    answer = get_answer(context, question)

    item["context"] = context
    item["question"] = question
    item["answers"] = answer

# Save the modified data back to the same file
with open("output/exp_eng_short.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write("\n")

print("Answers have been added to 'output/exp_eng_short.jsonl'.")
