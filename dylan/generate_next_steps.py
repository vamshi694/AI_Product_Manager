import connect_gemini
import re
import json

model = connect_gemini.access_model(temperature = 0.8)

# Generate next steps
def generate_next_steps(chat_conv_history, next_steps_file_name):  
    generated_next_steps = model.generate_content(f"Write down the next steps based on the conversation : {chat_conv_history}. Also based on the conversation, you as a technical product manager decide if you want to schedule another meeting with the user to gather more context.")
    
    with open (next_steps_file_name, "w") as f:
        next_steps_file = f.write(generated_next_steps.text)
    
    return next_steps_file