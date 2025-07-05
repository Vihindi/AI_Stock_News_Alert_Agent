import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def evaluate_impact(news_text):
    prompt = f"""
    Rate the market impact of this stock-related news on a scale from 1 (very low) to 5 (very high).
    News: "{news_text}"

    Return only a single digit number.
    """
    response = model.generate_content(prompt)
    score = response.text.strip()[0]
    try:
        return int(score)
    except:
        return 1
