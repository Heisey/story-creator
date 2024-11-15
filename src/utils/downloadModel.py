
from transformers import AutoTokenizer, AutoModelForCausalLM
import os


def downloadModel(model_name):
  print('Starting model download')
  save_directory = 'src/models/' + model_name
  os.makedirs(save_directory, exist_ok=True)

# Download the tokenizer and model to the specified directory
  # model_name = "mosaicml/mpt-7b-storywriter"

  tokenizer = AutoTokenizer.from_pretrained(model_name)
  tokenizer.save_pretrained(save_directory)

  model = AutoModelForCausalLM.from_pretrained(
      model_name,
      torch_dtype="auto",  # Automatically determine the data type (e.g., float16 for efficiency)
      trust_remote_code=True  # Allow loading of models with custom code
  )
  model.save_pretrained(save_directory)

  print('Finished model download')