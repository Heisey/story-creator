
import jobs

def generatePage(character_data, initial_context, num_panels=6):
    """Generate a single comic book page with multiple panels."""
    page = []
    context = initial_context
    
    for i in range(num_panels):
        # Create a varied prompt by asking for a specific scene progression and referencing prior events
        panel_prompt = (
          f"{context}\n\n"
          f"Panel {i+1}: Generate a unique event in the story that hasn't occurred in previous panels. "
          f"{character_data['name']} should face a new development related to the ongoing mystery. "
          "Make sure this scene doesn’t repeat previous panels."
        )
        
        # Generate and store panel
        panel_text = jobs.generatePanel(panel_prompt)
        page.append(panel_text)
        
        # Update context to include this panel’s narrative for continuity
        context += f" Panel {i+1}: {panel_text}"
        
    return page