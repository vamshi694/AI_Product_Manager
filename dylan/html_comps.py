import streamlit as st

def chat_input_html():
    chat_input_html = f"""
                        <style>
                            [data-testid = "stChatInput"]{{
                                max-height: 65px; /* Adjust this value to your desired max height */
                                overflow-y: auto;
                            }}
                        </style>
                    """
    return st.markdown(chat_input_html, unsafe_allow_html = True)

def avatar_html(url):
    video_html = f"""
            <video  width="100%" height="225%" src="{url}" controls autoplay>
                Your browser does not support the video tag.
            </video>
        """
    return st.markdown(video_html, unsafe_allow_html = True)

def bg_html(default_bg_image):
    bg_html = f"""
            <style>
                .st-emotion-cache-uf99v8{{
                    background-image : url("data:image/gif;base64,{default_bg_image}");
                }}
            </style>
            """
    return st.markdown(bg_html, unsafe_allow_html = True)

def bg_none_html():
    email_html = f"""
                <style>
                    .st-emotion-cache-uf99v8{{
                        background-image : none;
                    }}
                </style>
                """
    return st.markdown(email_html, unsafe_allow_html = True)

def app_html(default_bg_image):
    app_html = f"""
            <style>
                    .st-emotion-cache-uf99v8{{
                        background-color: black;
                        background-image : url("data:image/gif;base64,{default_bg_image}"); 
                        /*background-image: url("https://www.thesun.co.uk/wp-content/uploads/2021/10/2394f46a-c64f-4019-80bd-445dacda2880.jpg?w=670");   */        
                        background-size: contain;
                        background-repeat: no-repeat;
                        background-position: center;
                        width:100%;
                        height:auto;
                    }}
                    .st-emotion-cache-6qob1r{{
                        background-color: black;
                        border-right: 0.3px solid grey;
                    }}  
                    .st-emotion-cache-6qob1r {{
                        overflow: hidden;
                        min-width: 390px;
                    }}
                    .st-emotion-cache-16txtl3 {{
                        padding: 1rem 1rem
                    }}
                    .st-bc {{
                        background-color: rgb(250, 250, 250);
                        color: black;
                    }}
                    .st-bv {{
                        caret-color: black;
                    }}
                    .st-emotion-cache-16txtl3 h1 {{
                        font-size: 75px;
                        font-weight: 600;
                        text-align: center;
                        padding:0px;
                    }}
                    .st-emotion-cache-16txtl3 h2 {{
                        padding: 0px;
                        text-align: center;
                    }}
                    [data-testid = "stHorizontalBlock"]{{
                        margin-left: 14px;
                    }}
            </style>
            """
    return st.markdown(app_html, unsafe_allow_html = True)


