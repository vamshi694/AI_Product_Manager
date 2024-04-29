import connect_gemini
import re
import json

model = connect_gemini.access_model(temperature = 0.8)

# Generate user stories for the generated epic
def generate_user_stories(chat_conv_history, generated_epic):

    user_stories = model.generate_content(f"Create 2 user stories for the requested feature based on the conversation and the epic created: {chat_conv_history} + {generated_epic}. Respond in JSON format only. List of dictionaries with each dictionary consisting of 'user_story_name' as key and 'user_story_description' as value. No subheadings. No additional text or explanations are required.")
    user_stories_json = re.sub(r'`','',re.sub('json','', re.sub('\n','', user_stories.text)))
    generated_user_stories = json.loads(user_stories_json)

    return generated_user_stories
    # return user_stories
    # user_stories = model.generate_content(f"Create 2 user stories for the requested feature based on the conversation and the epic created: {chat_conv_history} + {generated_epic}. The format of the output should be a list of dictionaries with each dictionary consisting of 'user_story_name' as key and 'user_story_description' as value. No subheadings.")
    # user_stories_json = re.sub(r'`','',re.sub('json','', re.sub('\n','', user_stories.text)))
    # generated_user_stories = json.loads(user_stories_json)

    # return generated_user_stories