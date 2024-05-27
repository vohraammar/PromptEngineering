# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:48:39 2024

@author: Brain Hacker
"""

#%%
import google.generativeai as genai
GOOGLE_API_KEY = 'AIzaSyDaZQujJc-ejLkRD11Vvx6_Sc7FbTEwvn8'
genai.configure(api_key=GOOGLE_API_KEY)
#%%
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
#%%
model = genai.GenerativeModel('gemini-pro')
#%%
import textwrap
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
#%%
response = model.generate_content(
    """You are a seasoned efficiency consultant, renowned for developing ingenious life hacks specifically for busy professionals. (Think about the specific challenges professionals face)

A client has approached you today, overwhelmed by the feeling of being constantly behind on emails, meetings, and to-do lists. They juggle a demanding job with personal commitments and feel like they're constantly playing catch-up. (Think about the specific pain points of a busy professional)
    
Here's what you need to consider when crafting your life hack:

    Identify a common pain point: What are some everyday tasks that busy professionals find tedious, time-consuming, or frustrating? (e.g., scheduling meetings, managing to-do lists, information overload from emails) (Added example)
    Originality is key: Don't offer generic advice. Think outside the box and develop a unique approach.
    Practicality matters: The solution should be easy to implement and integrate into daily life.
    Focus on efficiency: The life hack should save time, effort, or resources.

Now, get creative! Craft a life hack or productivity tip that will leave your client feeling empowered and in control of their day.

Additional prompts to guide your brainstorming (using few-shot examples):

    What everyday task could be simplified by repurposing a common object? (Example: Can a paperclip be used to create a visual priority system for to-do list items?)
    How could you utilize technology to automate a mundane chore? (Example: Can a scheduling app be integrated with email to automatically suggest meeting times based on everyone's availability?)
    Can you develop a clever system to organize and prioritize tasks? (Example: Can a "batching" system be implemented to group similar tasks together and work on them efficiently?)
    Is there a way to combine multiple tasks into a single, efficient action? (Example: Can a voice memo app be used to capture notes while walking to a meeting?)

Remember, your client seeks a unique and practical solution. Use your expertise to design a life hack that will transform their daily routine!"""
)

to_markdown(response.text)

#%%
