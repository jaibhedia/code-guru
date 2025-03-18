from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = ""

class CodeRequest(BaseModel):
    user_input: str

@app.post("/generate_letter/")
async def generate_letter(request: CodeRequest):
    # Bas ek ek letter return karega
    next_char = request.user_input.strip()[-1] if request.user_input else ""
    
    if not next_char:
        return {"next_letter": "Start typing..."}

    # AI se puchh ke hint bhi de sakte hain
    ai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Code likhne ka agla akshar kya hona chahiye: {request.user_input}"}]
    )

    return {
        "next_letter": next_char,
        "hint": ai_response["choices"][0]["message"]["content"]
    }
