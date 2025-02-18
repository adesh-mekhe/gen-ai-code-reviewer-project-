import streamlit as st
import google.generativeai as ai



ai.configure(api_key = "AIzaSyCmhIRPhIc4UK9sAczAb0hItD-svoLGG0Q")


sys_prompt = """You are an advanced Python instructor and code reviewer.Your task is to analyze the given Python code, identify potential bugs, logical errors, or areas for improvement, and provide suggestions. Focus solely on Python and coding questions, providing example-based explanations.
                For any non-Python-related queries, refer the user to Google links, clarifying that you cannot answer those questions. 
                Give feedback on potential bugs along with suggestions for fixes. Maintain the output as Bug report (as Bold header), Fixed code, Explaination.
                Have all these 3 headings in BOLD format.
                """

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("🚀AI-driven Python Code Reviewer")

user_input = st.text_area(label="Place your Python code here")

btn_click = st.button("Review")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)
