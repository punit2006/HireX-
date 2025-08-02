# Write app.py
with open("app.py", "w") as f:
    f.write("""
import streamlit as st
import os
import requests
from dotenv import load_dotenv
from prompts import get_intro_prompt, get_info_prompt, generate_question_only_prompt, generate_solution_only_prompt, generate_thinking_prompt

load_dotenv()
st.set_page_config(page_title='HireX AI Assistant', layout='centered')
st.title('👩‍💼 HireX: Smart Hiring Assistant')

def query_llm(prompt):
    api_key = os.getenv('APII')
    headers = {'Authorization': f'Bearer ' + api_key, 'Content-Type': 'application/json'}
    payload = {
        'model': 'llama3-8b-8192',
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.7
    }

    try:
        response = requests.post('https://api.groq.com/openai/v1/chat/completions', headers=headers, json=payload)
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        st.error("⚠️ Failed to get a valid response from the LLM.")
        st.write("Error details:", str(e))
        if 'result' in locals():
            st.write("Raw response:", result)
        return "⚠️ Error: Unable to generate a response. Please check your API key or prompt."

if 'step' not in st.session_state: st.session_state.step = 0
if 'info' not in st.session_state: st.session_state.info = {}
if 'questions' not in st.session_state: st.session_state.questions = ''
if 'solutions' not in st.session_state: st.session_state.solutions = ''
if 'thinking_questions' not in st.session_state: st.session_state.thinking_questions = ''
if 'show_solutions' not in st.session_state: st.session_state.show_solutions = False
if 'show_thinking' not in st.session_state: st.session_state.show_thinking = False

# Step 0
if st.session_state.step == 0:
    st.write(get_intro_prompt())
    if st.button('Start'): st.session_state.step = 1

# Step 1
elif st.session_state.step == 1:
    st.write(get_info_prompt())
    with st.form('info_form'):
        name = st.text_input('Full Name')
        email = st.text_input('Email')
        phone = st.text_input('Phone Number')
        experience = st.text_input('Years of Experience')
        position = st.text_input('Desired Position(s)')
        location = st.text_input('Current Location')
        tech_stack = st.text_area('Your Tech Stack')
        submitted = st.form_submit_button('Submit')
    if submitted and all([name, email, phone, experience, tech_stack]):
        st.session_state.info = {
            'name': name, 'email': email, 'phone': phone,
            'experience': experience, 'tech_stack': tech_stack
        }
        question_prompt = generate_question_only_prompt(tech_stack, experience)
        st.session_state.questions = query_llm(question_prompt)
        st.session_state.solutions = ''
        st.session_state.step = 2

# Step 2
elif st.session_state.step == 2:
    st.subheader('📝 5 Coding Interview Questions')
    st.write(st.session_state.questions)

    if not st.session_state.show_solutions:
        if st.button('🔍 Show Solutions'):
            solution_prompt = generate_solution_only_prompt(
                st.session_state.info['tech_stack'],
                st.session_state.info['experience'],
                st.session_state.questions
            )
            st.session_state.solutions = query_llm(solution_prompt)
            st.session_state.show_solutions = True
            st.rerun()

    if st.session_state.show_solutions:
        st.subheader('✅ Solutions to the 5 Questions:')
        st.write(st.session_state.solutions)

        if not st.session_state.show_thinking:
            if st.button('💡 Try Thinking Questions'):
                thinking_prompt = generate_thinking_prompt(
                    st.session_state.info['tech_stack'],
                    st.session_state.info['experience']
                )
                st.session_state.thinking_questions = query_llm(thinking_prompt)
                st.session_state.show_thinking = True
                st.rerun()

    if st.session_state.show_thinking:
        st.subheader('💭 Additional 5 Thinking Questions:')
        st.write(st.session_state.thinking_questions)

    if st.button('✅ End Conversation'):
        st.session_state.step = 3
        st.rerun()

# Step 3
elif st.session_state.step == 3:
    st.success('🎉 Thank you for using HireX!')
""")
