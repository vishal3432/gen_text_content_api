from transformers import GPT2LMHeadModel,GPT2Tokenizer
from datasets import Dataset
from preprocess import load_dataset

model_name = "distilgpt2"

tokenizer= GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

texts = load_dataset()


dataset = Dataset.from_dict({"text":texts})

def tokenize(example):
  return tokenizer(example["text"],truncation=True,max_length = 128)

dataset = dataset.map(tokenize,batched=True)


from transformers import Trainer,TrainingArguments

training_args = TrainingArguments(
  output_dir = "./model",
  overwrite_output_dir = True,
  num_train_epchos = 1,
  per_device_train_batch_size=1,
  save_steps = 500,
  save_total_limit = 2
)

trainer = Trainer(
  model=model,
  args=training_args,
  tain_dataset=dataset
)

trainer.train()

model.save_pretrained("./model")
tokenizer.save_pretrained("./model")