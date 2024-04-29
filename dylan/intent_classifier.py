import connect_gemini

model = connect_gemini.access_model(temperature = 0.8)

# Classify the intent of the conversation as either "Feature request" or "New idea brainstorming"
def intent_classifier(chat_conv_history):
    
    intent_classification_tag = model.generate_content(f"Classify the intent of the conversation as one of the following: [New feature request, New product idea]. Just print the category : {chat_conv_history}")
    
    return str(intent_classification_tag.text.rstrip())