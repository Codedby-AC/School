from google import genai

# =========================================
# CLIENT
# =========================================

client = genai.Client(
    api_key="AIzaSyDZqNi1o7iaJdKm-4g4zoMV5nQG8pFi4MA"
)

# =========================================
# SHIKSHA AI
# =========================================

def ask_shiksha_ai(question):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""

You are Shiksha AI.

You help students in:
- coding
- AI
- mathematics
- assignments
- psychology
- exams

Give short helpful answers.

Student Question:
{question}

"""
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"