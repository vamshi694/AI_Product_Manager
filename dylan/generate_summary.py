import connect_gemini

model = connect_gemini.access_model(temperature = 0.8)

# Generate Summary
def summarizer(chat_conv_history, summary_file_name):
    
    summary = model.generate_content(f"Summarize the conversation: {chat_conv_history}")
    
    with open (summary_file_name, "w") as summary_file:
        summary_file = summary_file.write(summary.text)
    
    return summary_file

