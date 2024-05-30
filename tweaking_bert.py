#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:18:48 2024

@author: RalfsArvids123
"""

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

# Load dataset (replace with your own or BoolQ)
dataset = load_dataset("super_glue", "boolq") 

# Load pre-trained model and tokenizer
model_name = "bert-base-cased" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare data for training
def tokenize_function(examples):
    return tokenizer(examples["question"], examples["passage"], truncation=True, padding="max_length")

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",  
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,         
    weight_decay=0.01,
)

# Create Trainer and start training
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
)

trainer.train()
