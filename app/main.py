from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AutoContentTool")

class GenerateRequest(BaseModel):
    text: str

class GenerateResponse(BaseModel):
    original: str
    generated: str

@app.post("/generate", response_model=GenerateResponse)
def generate_content(payload: GenerateRequest):
    # Simple placeholder logic
    generated_text = f"Processed version of: {payload.text}"

    return GenerateResponse(
        original=payload.text,
        generated=generated_text
    )
