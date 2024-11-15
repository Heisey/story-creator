
def fillCharacterDetails(character, prompt_template):
    """Fill placeholders in the prompt template with character details."""
    
    # Dictionary mapping placeholders to character details
    replacements = {
        "{{name}}": character.get("name", "the main character"),
        "{{age}}": str(character.get("age", "unknown age")),
        "{{role}}": character.get("role", "unknown role"),
        "{{traits}}": ", ".join(character.get("traits", [])),
        "{{backstory}}": character.get("backstory", ""),
        "{{motivations}}": character.get("motivations", ""),
    }
    
    # Replace placeholders in the prompt template
    filled_prompt = prompt_template
    for placeholder, value in replacements.items():
        filled_prompt = filled_prompt.replace(placeholder, value)
    
    return filled_prompt

