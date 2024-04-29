import connect_gemini
import re
import json

model = connect_gemini.access_model(temperature = 0.8)

# Classify the intent of the conversation as either "Feature request" or "New idea brainstorming"
def intent_classifier(chat_conv_history):
    
    intent_classification_tag = model.generate_content(f"Classify the intent of the conversation as one of the following: [New feature request, New product idea]. Just print the category : {chat_conv_history}")
    
    return str(intent_classification_tag.text.rstrip())

# Generate Summary
def summarizer(chat_conv_history, summary_file_name):
    
    summary = model.generate_content(f"Summarize the conversation: {chat_conv_history}")
    
    with open (summary_file_name, "w") as summary_file:
        summary_file = summary_file.write(summary.text)
    
    return summary_file

# Generate next steps
def generate_next_steps(chat_conv_history, next_steps_file_name):  
    generated_next_steps = model.generate_content(f"Write down the next steps based on the conversation : {chat_conv_history}. Also based on the conversation, you as a technical product manager decide if you want to schedule another meeting with the user to gather more context.")
    
    with open (next_steps_file_name, "w") as f:
        next_steps_file = f.write(generated_next_steps.text)
    
    return next_steps_file

# Generate user stories for the generated epic
def generate_user_stories(chat_conv_history, generated_epic):

    user_stories = model.generate_content(f"Create 2 user stories for the requested feature based on the conversation and the epic created: {chat_conv_history} + {generated_epic}. Respond in JSON format only. List of dictionaries with each dictionary consisting of 'user_story_name' as key and 'user_story_description' as value. No subheadings. No additional text or explanations are required.")
    user_stories_json = re.sub(r'`','',re.sub('json','', re.sub('\n','', user_stories.text)))
    generated_user_stories = json.loads(user_stories_json)

    return generated_user_stories

# Generate epic
def generate_epic(chat_conv_history):
    
    epic = model.generate_content(f"Just create an epic for the requested feature based on the conversation : {chat_conv_history}. The output should be a dictionary with epic_name as key and epic_description as value.")
    epic_json = re.sub(r'`','',re.sub('json','', re.sub('\n','', epic.text)))
    generated_epic = json.loads(epic_json)
    
    return generated_epic

chat_model = model.start_chat(history=[])