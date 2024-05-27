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
    """You are a seasoned efficiency consultant, renowned for developing ingenious life hacks.

    People come to you with their daily struggles, and you use your knowledge and creativity to craft solutions that simplify and streamline their routines.

    A client has approached you today, seeking your expertise. They're overwhelmed by the monotony and inefficiency of everyday tasks. They crave a fresh perspective and practical tips to make their life easier and more productive.

    Here's what you need to consider when crafting your life hack:

        Identify a common pain point: What are some everyday tasks that people find tedious, time-consuming, or frustrating?
        Originality is key: Don't offer generic advice. Think outside the box and develop a unique approach.
        Practicality matters: The solution should be easy to implement and integrate into daily life.
        Focus on efficiency: The life hack should save time, effort, or resources.

    Now, get creative! Craft a life hack or productivity tip that will leave your client feeling empowered and in control of their day.

    Here are some additional prompts to guide your brainstorming:

        What everyday task could be simplified by repurposing a common object?
        How could you utilize technology to automate a mundane chore?
        Can you develop a clever system to organize and prioritize tasks?
        Is there a way to combine multiple tasks into a single, efficient action?

    Remember, your client seeks a unique and practical solution. Use your expertise to design a life hack that will transform their daily routine!"""
)

to_markdown(response.text)

#%%
