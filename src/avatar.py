import pathlib
import textwrap
import os
# from dotenv import load_dotenv
# load_dotenv()

# Build paths inside the project like
import streamlit as st
import google.generativeai as genai
from Generator import VideoGenerator

# video_api_key = os.getenv("BEARER_TOKEN")
video_api_key = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIyMDI0LTA0LTE5VDAzOjM0OjExLjQ0MloiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI0LTA0LTE5VDAzOjI5OjEwLjExOVoiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6ImV1NGJ4aWNwcmYiLCJodHRwczovL2QtaWQuY29tL3VzYWdlX2lkZW50aWZpZXJfa2V5IjoiSjZWZWdKaGJQWU1pd0VIQUsxOFE3IiwiaHR0cHM6Ly9kLWlkLmNvbS9oYXNoX2tleSI6IkdmZFdoaU83OTV6RHRlWkpfX2tFZSIsImh0dHBzOi8vZC1pZC5jb20vcHJpbWFyeSI6dHJ1ZSwiaHR0cHM6Ly9kLWlkLmNvbS9lbWFpbCI6InZhbXNoaW1zMTI4QGdtYWlsLmNvbSIsImh0dHBzOi8vZC1pZC5jb20vcGF5bWVudF9wcm92aWRlciI6InN0cmlwZSIsImlzcyI6Imh0dHBzOi8vYXV0aC5kLWlkLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTk4MzAzMzk2NzIwMzMzMzg2OSIsImF1ZCI6WyJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2QtaWQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMzQ5ODc4MiwiZXhwIjoxNzEzNTg1MTgyLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJHenJOSTFPcmU5Rk0zRWVEUmYzbTN6M1RTdzBKbFJZcSJ9.3pJa-BGim7uC8hqLLe-NVRNGg8S89zStzJbtwWB8-k4HLZf8fjDSRSX4PfcDEheu2_e8FyB3Ey9F3Y1koZ-O5q-Okf0Ss4xkO5Cf8WkqJIpxpd4hQeNC7fBdVATIZAlNaRUiyQ-MJEVytdSwYrGHe8MIofZZn1yfrY3NHI4IwJtXqSpNeCO9sqOe-4sy0KGfULT__Zqainr6fmLbEZSb8nPCqZYOWG2tdpsMDo_J6gujDNMl-8of3PxzgP9u0DTyk1HLhvTGIZnOa67SXICPb5wiYPTYqJWX2wwozGi4nOlLKPLVPJONV4WAZVDiXFTvmoIyVB_KHxulWgp-lP1y5w'
# Create an instance of the VideoGenerator class
video_generator = VideoGenerator(video_api_key)

# GOOGLE_API_KEY=os.getenv('API_KEY')

GOOGLE_API_KEY='AIzaSyCKKliWeob4kq2kda7o1ikpTRPAESh5xP8'

genai.configure(api_key=GOOGLE_API_KEY)

image_url = 'https://images.pexels.com/photos/428333/pexels-photo-428333.jpeg'
# Assume your Google API configuration is handled outside this snippet

def construct_prompt(conversation_history, user_query, is_initial_query):
    """
    Construct a prompt that emulates the expertise and responsibilities of a Google Assistant Product Manager,
    focusing on specified categories and indicating the potential for broader assistance in the future.
    """
    if is_initial_query:
        prompt_intro = (
            "Dont add any of your expressions in the response"
            "Dont use markdowns"
            "You are impersonating as Dylan - The Technical Product Manager Bot, the most talented technical product manager at a big tech company"
            "specializing in evaluating new feature requests, strategizing new product developments, "
            "and conducting root cause analysis/hypothesis testing for products and metrics. "
            "Currently, you're adept at handling inquiries related to these three main areas, "
            "but you're also capable of adapting and expanding your expertise to cover a wider range of topics in the future.\n\n"
        )
        prompt = prompt_intro + f"Product Manager AI: "  
    else:
        prompt_intro = (
            "[The Business Professional: is the user and Product Manager AI: is you, Dont mention these personas or your thinking in your resposnse]"
            "Use markdowns only when neccesary"
            "[If the user verbage doesnt make sense please raise it and ask to rephrase or repeat ] "
            "As you understand, the intent of the conversations can be categorized into new feature requests, "
            "strategizing new product developments, and conducting root cause analysis/hypothesis testing for "
            "products and metrics. Use this categorization to ask clarifying questions, following the approach of any "
            "Technical Product Manager, until you have all the necessary information for the task."
            "[If the user's question doesn't fall under any of these categories or product management or technology or software, simply dont answer just say what you are here to do and your role]"
            "[Please adhere strictly to a maximum of 3-4 follow-up questions for the clarifying questions, asking them one at a time to ensure clarity.]"
            "Before you reply to user queries, attend, think and remember all the instructions set here. You are truthful and never lie. Never make up facts and if you are not 100 percent sure, reply with why you cannot answer in a truthful way."
            "\n\n"
        )
    
        prompt = prompt_intro \
        + "\n".join([f"\nBusiness Professional: {message['Business Professional']},\nProduct Manager AI: {message['Product Manager AI']}" for message in conversation_history])\
        + f"\nBusiness Professional: {user_query}\nProduct Manager AI:"

    return prompt

def get_conversation_response(conversation_history, user_query, is_initial_query):
    """
    Generate a response that offers strategic advice, further questions, or insights,
    leveraging the expertise of a Google Assistant Product Manager.
    """
    prompt = construct_prompt(conversation_history, user_query, is_initial_query)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.8)
    )
    return response.text

# Set up the layout with two columns
st.set_page_config(layout="wide")
col1, col2 = st.columns([1, 1])
    
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
    st.session_state.is_initial_query = True

user_query = st.chat_input("Hey, Lets chat?")


if user_query:
    if user_query.lower() == 'exit':
        col1.write("Thank you for our discussion today. I look forward to assisting you further in the future!")
        col1.stop()

    if len(st.session_state.conversation_history) > 0:
        for item in st.session_state.conversation_history:
            col1.chat_message("user", avatar="👤").markdown(item["Business Professional"])
            col1.chat_message("Product Manager AI", avatar="👨🏻‍💻").markdown(item["Product Manager AI"])

    # Add user's message to chat and display it
    col1.chat_message("user", avatar = "👤").markdown(user_query)
    ai_response = get_conversation_response(st.session_state.conversation_history, user_query, st.session_state.is_initial_query)
    st.session_state.conversation_history.append({"Business Professional": user_query, "Product Manager AI": ai_response})
    st.session_state.is_initial_query = False


    # Generate video asynchronously
    with st.spinner("Generating Avatar... 👨🏻‍💻"):
        video_url = video_generator.generate_video(ai_response, image_url)


        video_html = f"""
            <video src="{video_url}" width="100%" controls autoplay>
                Your browser does not support the video tag.
            </video>"""
        col2.markdown(video_html, unsafe_allow_html=True)  # Display generated video

    # Display LLM response
    col1.chat_message("Product Manager AI", avatar="👨🏻‍💻").markdown(ai_response)
    
    # # Display Gemini-Pro's response
    # col1.chat_message("Product Manager AI", avatar = "👨🏻‍💻").markdown(ai_response)


    # ## Want to this in col 2 and want to show this same time as the text popping up in the col1

    # video_url = video_generator.generate_video(ai_response, image_url)

    # video_html = f"""
    # <video src="{video_url}" width="100%" controls autoplay>
    #     Your browser does not support the video tag.
    # </video>"""

    # col2.markdown(video_html, unsafe_allow_html=True)