from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_dir = "src/models/flan_t5_base"  # Path to your saved model directory
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

# Define function to generate text with updated generation settings
def generate_text(prompt, max_length=300):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        repetition_penalty=1.5
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Define the story prompts by section for each page
def create_section_prompt(section, character_data, page_range):
    """Generate a story prompt for each story section and page range."""
    prompt = (
        f"This is a comic book story set in Willowbrook featuring {character_data['name']}, a {character_data['age']}-year-old "
        f"{character_data['role']}. {character_data['name']} is {', '.join(character_data['traits'])}.\n\n"
        f"Section: {section}\n"
        f"Pages: {page_range}\n\n"
        "Outline a series of events across these pages that develop the mystery of the silver locket in Willowbrook. "
        "Describe each page’s panels with new discoveries, character actions, and interactions with townsfolk. "
        "Ensure the narrative is engaging, introducing settings and challenges that move the story forward."
    )
    return prompt

# Generate the story by section and pages
def generateBook(character_data):
    story = {}

    # Page allocations
    sections = {
        "Introduction": (1, 1),
        "Investigation": (2, 7),
        "Complications": (8, 13),
        "Climax": (14, 18),
        "Resolution": (19, 20)
    }

    # Generate story for each section and page range
    for section, (start_page, end_page) in sections.items():
        page_range = f"Pages {start_page}-{end_page}"
        prompt = create_section_prompt(section, character_data, page_range)
        section_text = generate_text(prompt)
        
        # Split section text across allocated pages
        for page_num in range(start_page, end_page + 1):
            print(f'generating page {page_num}...')
            story[f"Page {page_num}"] = [section_text]

    return story