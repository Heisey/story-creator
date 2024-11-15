from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import glob
import os
from datasets import Dataset

import utils

model_dir = "src/models/flan_t5_base"  # Path to your saved model directory
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
data_dir = "src/data/training"


def preprocess_function(examples):
    model_inputs = tokenizer(examples["input_texts"], max_length=512, truncation=True, padding="max_length")
    labels = tokenizer(examples["output_texts"], max_length=512, truncation=True, padding="max_length").input_ids
    model_inputs["labels"] = labels
    return model_inputs

def createModel(output_dir):
  print('Creating Model')

  dataset = []
  for file_path in sorted(glob.glob(os.path.join(data_dir, "*.json"))):
      data = utils.loadJson(file_path)
      dataset.append(data)

  input_texts = []
  output_texts = []

  for story in dataset:
    for panel in story["story"]:
      input_texts.append(panel["input"])
      
      # Format output by combining different elements for generation
      output_parts = [
        f"Panel Type: {panel['output'].get('Panel Type', '')}",
        f"Setting: {panel['output'].get('Setting', '')}",
        f"Character Action: {panel['output'].get('Character Action', '')}",
        f"Dialogue: {panel['output'].get('Dialogue', '')}",
        f"Narration: {panel['output'].get('Narration', '')}"
      ]
      output_texts.append(" | ".join(output_parts))

  
  dataset_dict = {"input_texts": input_texts, "output_texts": output_texts}
  comic_dataset = Dataset.from_dict(dataset_dict).map(preprocess_function, batched=True)

  model.save_pretrained(output_dir)
  tokenizer.save_pretrained(output_dir)

  print(f"Model saved to {output_dir}")
  return output_dir
  return comic_dataset