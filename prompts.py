with open("prompts.py", "w") as f:
  f.write('''def get_intro_prompt():
    return """👋 Welcome to **HireX** – your smart AI Hiring Assistant!
We're here to generate technical interview questions tailored to your skills and experience.
Let’s get started with a few quick details."""

ef get_intro_prompt():
    return """👋 Welcome to **HireX** – your smart AI Hiring Assistant!
We're here to generate technical interview questions tailored to your skills and experience.
Let’s get started with a few quick details."""

def get_info_prompt():
    return """
Please fill out the following details to help us customize your interview questions:
1. Full Name
2. Email
3. Phone Number
4. Years of Experience
5. Desired Position(s)
6. Current Location
7. Your Tech Stack (comma-separated)
"""

def generate_question_only_prompt(tech_stack, experience):
    return f"""
Generate 5 **technical coding interview questions only** (no answers) for someone with {experience} years of experience in the following tech stack:

{tech_stack}

The questions should test coding ability — logic, implementation, algorithms, or systems — using the mentioned technologies.

Respond only in this format:
1. **Question:** ...
2. **Question:** ...
3. **Question:** ...
4. **Question:** ...
5. **Question:** ...
"""

def generate_solution_only_prompt(tech_stack, experience, questions):
    return f"""
You are an AI coding interview assistant.

Generate answers to the following 5 coding interview questions for someone with {experience} years of experience in:

Tech Stack: {tech_stack}

Each answer must include:
- ✅ Complete, executable code in the tech stack mentioned
- ✅ Brief explanation of what the code does and why

Questions:
{questions}

Format:
1. **Answer:**
```{tech_stack.lower()}
# your code here

Respond in this format:
1. **Answer:** ...
2. **Answer:** ...
3. **Answer:** ...
4. **Answer:** ...
5. **Answer:** ...
"""

def generate_thinking_prompt(tech_stack, experience):
    return f"""
Generate 5 advanced or creative "thinking" (open-ended, discussion) interview questions for someone with {experience} years of experience in {tech_stack}.
Number and return questions only, without answers.
"""''')
