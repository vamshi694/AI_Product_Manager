import connect_gemini

model = connect_gemini.access_model(temperature = 0.8)

chat_model = model.start_chat(history=[])