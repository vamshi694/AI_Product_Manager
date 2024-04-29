import streamlit as st
from generative_ai_utils import chat_model, summarizer, generate_epic, generate_user_stories, generate_next_steps, intent_classifier
from avatar import generate_video
from mail import send_email
from jira_tasks import create_jira_epic, create_jira_user_story
from html_comps import chat_input_html, app_html, bg_html, bg_none_html
from encode_images import encode_gif, encode_image_url
from role_emoji import change_role, emoji
import prompts
import time

summary_file_name = "summary.txt"
next_steps_file_name = "next_steps.txt"
project_name = "KAN"

def main():
    bg_image = encode_image_url("https://www.thesun.co.uk/wp-content/uploads/2021/10/2394f46a-c64f-4019-80bd-445dacda2880.jpg?w=670") #Initail background image
    
    with st.sidebar:
        st.title("Dylan")
        st.header("The Product Manager Bot")
        st.markdown("###")
        st.markdown("###")
        
        messages = st.container(height = 420, border = False) #Chat history container
        #Displays chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = chat_model
        conv_history = st.session_state.chat_history.history
        for each_message in conv_history:
            with messages.chat_message(change_role(each_message.role), avatar = emoji(each_message.role)):
                if len(each_message.parts)>1:
                    st.write(each_message.parts[-1].text)
                else:
                    st.write(each_message.parts[0].text)

        #A prompt to tune the model's response
        instruction = prompts.chat_model_instruction

        if "initial_user_query" not in st.session_state:
            st.session_state.initial_user_query = True

        col1, col2 = st.columns([0.85,0.15])
        with col1:
            user_query = st.chat_input("How can I help you today?")
            chat_input_html()

        with col2:
            if st.session_state.initial_user_query == True:
                end_conv = st.button("🛑", type = "primary", disabled = True)
            else:
                end_conv = st.button("🛑", disabled = False, help = "Click to end conversation and generate summary, epics, next steps, etc.,")

        if user_query:
            bg_image = encode_gif("images/thinking.gif")
            #Display user's query
            with messages.chat_message("user", avatar = "👤"):
                st.write(user_query)   
            chat_model_response = st.session_state.chat_history.send_message([instruction, user_query])
            chat_model_response_text = chat_model_response.text 
        app_html(default_bg_image = bg_image) #Background gif when the model is processing the user's query
    #Display model's response in the form of text and speech
    if user_query and chat_model_response_text:
        time.sleep(10)
        #Generates and displays a talking avatar to read the model's text response. 
        generate_video(chat_model_response_text, "https://www.thesun.co.uk/wp-content/uploads/2021/10/2394f46a-c64f-4019-80bd-445dacda2880.jpg?w=670")
        
        #Display the model's response in the form of text
        with messages.chat_message("assistant", avatar = "👨🏻‍💻"):     
            st.write(chat_model_response.text)
            chat_model_response_text = chat_model_response.text
        st.session_state.initial_user_query = False

    if end_conv and conv_history != []:
        bg_html(default_bg_image = encode_gif("images/processing.gif")) #Background gif when summary is being generated
        
        summarizer(conv_history, summary_file_name) #Generates the summary and creates a summary text file with the name "summary.txt"
        time.sleep(10)
        classify_conv = intent_classifier(conv_history) #Classifies the conversation

        if classify_conv == "New feature request":
            bg_html(default_bg_image = encode_gif("images/epic.gif")) #Background gif when summary is being generated
            generated_epic = generate_epic(conv_history) #Generates epic
            if generated_epic:
                bg_html(default_bg_image = encode_gif("images/jira_epic.gif")) #Background gif while adding epic to Jira
                epic_key = create_jira_epic(project_name, generated_epic["epic_name"], generated_epic["epic_description"]) #Creates an epic in Jira 
            
            if epic_key:
                bg_html(default_bg_image = encode_gif("images/user_story.gif")) #Background gif when user_stories are being generated
                time.sleep(5)
                generated_user_stories = generate_user_stories(conv_history, generated_epic) #Generate user_stories
                if generated_user_stories:
                    bg_html(default_bg_image = encode_gif("images/jira_user_story.gif")) #Background gif while adding user_stories to Jira
                    create_jira_user_story(project_name, epic_key, generated_user_stories) #Create user stories in Jira

            bg_html(default_bg_image = encode_gif("images/summary.gif")) #Background gif when summary is being generated
            summarizer(conv_history, summary_file_name) #Generates the summary and create a summary text file (summary.txt)
            send_email("Meeting Summary", "Hi there! \nAttached is the meeting summary.", [summary_file_name]) #Mail the summary file to the user
        
        if classify_conv == "New product idea":
            bg_html(default_bg_image = encode_gif("images/nxt_steps.gif")) #Background gif when summary is being generated
            generated_next_steps = generate_next_steps(conv_history, next_steps_file_name) #Generates next steps and creates a text file with the name "next_steps.txt"
            
            #Email's the conversation summary and next steps file to the user
            if generated_next_steps!= "None":
                send_email("Meeting Summary and Next Steps", "Hi there! \nAttached are the meeting summary and the next steps files.", [summary_file_name, next_steps_file_name])

        #Background image is replaced with the following text once the summary file is e-mailed to the user
        st.title("An email is sent to you with a summary of the conversation. Thank you!")
        bg_none_html()

if __name__ == "__main__":
    main()