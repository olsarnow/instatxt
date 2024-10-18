#!/usr/bin/env python3

from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))


cam = input("Camera Model (Canon EOS 3000):  ") or "Canon EOS 3000"
obj = input("Objective (28-90 mm Zoom):  ") or "28-90 mm Zoom"
loc = input("Location: ")  
year = input("Year (2024): ") or "2024"
month = input("Month: ") 
add = input("Additions: ") 

ai_system_message = f"I need your assistance! Write a text for an Instagram post in English, using simple language, in three sentences. The post should be written from the observer's perspective, with a neutral and professional tone. Begin with a sentence mentioning the location and date the picture was taken. Include 20 relevant hashtags, and avoid using the word 'my'; instead, use 'a' or similar alternatives. The context is that the speaker is a photographer. Always start with a sentence that includes the location and date the picture was taken. Start with location, year/month and the Camera model, objective. write 5 sentences "

ai_user_message = f"taken with {cam} with a lens {obj}, in {loc}, in the {month} of  {year},  {add} "



completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": ai_system_message},
        {"role": "user", "content": ai_user_message}
    ]
)

answer = (completion.choices[0].message.content)

print(answer)
