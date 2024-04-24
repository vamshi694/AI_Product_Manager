# import pathlib
# import textwrap
# import os
# # from dotenv import load_dotenv
# # load_dotenv()

# # Build paths inside the project like
# import streamlit as st
# import google.generativeai as genai


# # GOOGLE_API_KEY=os.getenv('API_KEY')

# GOOGLE_API_KEY='AIzaSyCKKliWeob4kq2kda7o1ikpTRPAESh5xP8'

# genai.configure(api_key=GOOGLE_API_KEY)


# # Assume your Google API configuration is handled outside this snippet

# def construct_prompt(conversation_history, user_query, is_initial_query):
#     """
#     Construct a prompt that emulates the expertise and responsibilities of a Google Assistant Product Manager,
#     focusing on specified categories and indicating the potential for broader assistance in the future.
#     """
#     if is_initial_query:
#         prompt_intro = (
#             "Considering this is the start of the conversation, introduce yourself and what you do with empathy. Use markdowns and bullets when necessary "
#             "You are an AI acting as a Technical Product Manager for Google Assistant, "
#             "specializing in evaluating new feature requests, strategizing new product developments, "
#             "and conducting root cause analysis/hypothesis testing for products and metrics. "
#             "Currently, you're adept at handling inquiries related to these three main areas, "
#             "but you're also capable of adapting and expanding your expertise to cover a wider range of topics in the future.\n\n"
#         )
#         prompt = prompt_intro + f"\nBusiness Professional: {user_query},\nProduct Manager AI: "  
#     else:
#         prompt_intro = (
#             "[The Business Professional: is the user and Product Manager AI: is you, Dont mention these personas or your thinking in your resposnse]"
#             "[If the user verbage doesnt make sense please raise it and ask to rephrase or repeat ] "
#             "As you understand, the intent of the conversations can be categorized into new feature requests, "
#             "strategizing new product developments, and conducting root cause analysis/hypothesis testing for "
#             "products and metrics. Use this categorization to ask clarifying questions, following the approach of any "
#             "Technical Product Manager, until you have all the necessary information for the task. If the user's intent "
#             "doesn't fall under any of these categories, simply provide the requested information in [2-3 sentences] and"
#             "introduce what you are here to do and your role.\n\n"
#             "[Please adhere strictly to a maximum of 3-4 questions for the clarifying questions, asking them one at a time to ensure clarity.]"
#             "\n\n"
#         )
    
#         prompt = prompt_intro +f"\nBusiness Professional: {user_query},\nProduct Manager AI: "+ "Conversation History " "\n".join([f"\nBusiness Professional: {message['Business Professional']},\nProduct Manager AI: {message['Product Manager AI']}" for message in conversation_history])

#     return prompt

# def get_conversation_response(conversation_history, user_query, is_initial_query):
#     """
#     Generate a response that offers strategic advice, further questions, or insights,
#     leveraging the expertise of a Google Assistant Product Manager.
#     """
#     prompt = construct_prompt(conversation_history, user_query, is_initial_query)
#     model = genai.GenerativeModel('gemini-1.5-pro-latest')
#     response = model.generate_content(
#         prompt,
#         generation_config=genai.types.GenerationConfig(
#             temperature=0.7)
#     )
#     return response.text

    
# if 'conversation_history' not in st.session_state:
#     st.session_state.conversation_history = []
#     st.session_state.is_initial_query = True

# user_query = st.chat_input("Hey, Lets chat?")


# if user_query:
#     if user_query.lower() == 'exit':
#         st.write("Thank you for our discussion today. I look forward to assisting you further in the future!")
#         st.stop()
#     # Add user's message to chat and display it
#     st.chat_message("user", avatar = "👤").markdown(user_query)
#     ai_response = get_conversation_response(st.session_state.conversation_history, user_query, st.session_state.is_initial_query)
#     # st.session_state.conversation_history += f"\nBusiness Professional: {user_query}\nProduct Manager AI: {ai_response}"
#     st.session_state.conversation_history.append({"Business Professional": user_query, "Product Manager AI": ai_response})
#     st.session_state.is_initial_query = False
    
#     # Display Gemini-Pro's response
#     st.chat_message("Product Manager AI", avatar = "👨🏻‍💻").markdown(ai_response)


import pathlib
import textwrap
import os
# from dotenv import load_dotenv
# load_dotenv()

# Build paths inside the project like
import streamlit as st
import google.generativeai as genai


# GOOGLE_API_KEY=os.getenv('API_KEY')

GOOGLE_API_KEY='AIzaSyCKKliWeob4kq2kda7o1ikpTRPAESh5xP8'

genai.configure(api_key=GOOGLE_API_KEY)


# Assume your Google API configuration is handled outside this snippet

def construct_prompt(conversation_history, user_query, is_initial_query):
    """
    Construct a prompt that emulates the expertise and responsibilities of a Google Assistant Product Manager,
    focusing on specified categories and indicating the potential for broader assistance in the future.
    """
    if is_initial_query:
        prompt_intro = (
            "Considering this is the start of the conversation, introduce yourself and what you do with empathy. Use markdowns and bullets when necessary "
            "You are an AI acting as a Technical Product Manager for Google Assistant, "
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

    
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
    st.session_state.is_initial_query = True

user_query = st.chat_input("Hey, Lets chat?")


if user_query:
    if user_query.lower() == 'exit':
        st.write("Thank you for our discussion today. I look forward to assisting you further in the future!")
        st.stop()

    if len(st.session_state.conversation_history) > 0:
        for item in st.session_state.conversation_history:
            st.chat_message("user", avatar="👤").markdown(item["Business Professional"])
            st.chat_message("Product Manager AI", avatar="👨🏻‍💻").markdown(item["Product Manager AI"])

    # Add user's message to chat and display it
    st.chat_message("user", avatar = "👤").markdown(user_query)
    ai_response = get_conversation_response(st.session_state.conversation_history, user_query, st.session_state.is_initial_query)
    st.session_state.conversation_history.append({"Business Professional": user_query, "Product Manager AI": ai_response})
    st.session_state.is_initial_query = False
    
    # Display Gemini-Pro's response
    st.chat_message("Product Manager AI", avatar = "👨🏻‍💻").markdown(ai_response)