from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv(".env")

genai.configure(api_key=(os.getenv("API_KEY")))

def access_model(temperature):
    config = genai.types.GenerationConfig(temperature = temperature)
    model = genai.GenerativeModel("gemini-1.5-pro-latest", generation_config = config)
    return model