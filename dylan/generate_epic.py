import connect_gemini
import re
import json

model = connect_gemini.access_model(temperature = 0.8)

# Generate epic
def generate_epic(chat_conv_history):
    
    epic = model.generate_content(f"Just create an epic for the requested feature based on the conversation : {chat_conv_history}. The output should be a dictionary with epic_name as key and epic_description as value.")
    epic_json = re.sub(r'`','',re.sub('json','', re.sub('\n','', epic.text)))
    generated_epic = json.loads(epic_json)
    
    return generated_epic