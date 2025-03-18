from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = "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"

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
