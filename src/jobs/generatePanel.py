from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_dir = "src/models/flan_t5_base"  # Path to your saved model directory
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

def generatePanel(prompt):
    # Tokenize the input prompt
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    
    # Generate the output
    outputs = model.generate(input_ids, max_length=100, num_beams=5, early_stopping=True)
    
    # Decode and return the result
    return tokenizer.decode(outputs[0], skip_special_tokens=True)




# Page 1

# Panel 1

# Wide Panel: Timmy and Poppy are standing at the edge of a dense forest. Timmy looks excited, holding a small map. Poppy, the dog, is wagging his tail, looking eager.

# Caption (Narration): "One day, Timmy found an old map in his attic."

# Timmy: "Come on, Poppy! The map says there’s a treasure in the forest!"

# Panel 2

# Close-Up: Timmy's hand holding the old map, which shows a path leading to a big "X" in the middle of the forest.

# Caption (Narration): "A treasure marked by a big X? Who could resist?"

# Panel 3

# Medium Panel: Poppy runs ahead excitedly, barking at the forest entrance.

# Poppy (Barking): "Woof! Woof!"

# Timmy (Smiling): "Slow down, Poppy! Wait for me!"

# Panel 4

# Side View: Timmy and Poppy walk into the forest together. Timmy looks confident, while Poppy sniffs around curiously.

# Caption (Narration): "And so, Timmy and Poppy stepped into the mysterious forest."

