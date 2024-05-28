# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:13:53 2024

@author: Mara
"""

from transformers import AutoModelForCausalLM, AutoTokenizer
import json

# Loading the model from Hugging Face 
model_name = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name) 


# function for reading JSONL file 
def read_jsonl(file_path): 
    with open(file_path, "r", encoding="utf-8") as file: 
        lines = file.readlines()
        return [json.loads(line) for line in lines]
    
# function to send prompt to model for yes/no asnwer 
ddef get_response(prompt): 
    modified_prompt = prompt + "\nAnswer with 'yes' or 'no':"
    inputs = tokenizer(modified_prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(inputs.input_ids, attention_mask=inputs.attention_mask,
                             max_new_tokens=10, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # extracting the answer 
    response_lower = response.lower()
   if "yes" in response_lower:
       return 1
   elif "no" in response_lower:
       return 0
   else:
       # Handle cases where the response is unclear
       return -1


# reading the prompts 
data = read_jsonl("explicit_output_shortened.jsonl")

# processing the prompts for answers
for item in data:
    prompt = item["filled_template"]
    response = get_response(prompt)
    item["decision"] = response  # Add decision directly to the item
    print(f"Decision: {response}")

# saving the modified data back to the same file (Overwrites the existing file)
with open("explicit_output_shortened.jsonl", 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print("Decisions have been added to 'explicit_output_shortened.jsonl.")