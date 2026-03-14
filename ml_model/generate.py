# import os
# from pathlib import Path
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# BASE_DIR = Path(__file__).resolve().parent
# MODEL_PATH = BASE_DIR/"model"

# STR_PATH = str(MODEL_PATH)
model = GPT2LMHeadModel.from_pretrained("./ml_model/model")
tokenizer = GPT2Tokenizer.from_pretrained("./ml_model/model")

def generate_text(prompt):
  inputs=tokenizer.encode(prompt, return_tensors="pt")
  
  outputs=model.generate(
    inputs,
    max_length=100,
    num_return_sequences=1,
    temperature=0.7
  )
  
  text = tokenizer.decode(outputs[0],skip_special_tokens=True)
  
  return text
  

print(generate_text("Write a blog intro about AI"))