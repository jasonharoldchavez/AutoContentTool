from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="AutoContentTool API",
    description="API for scoring and processing content (QIF-style).",
    version="1.0.0"
)

# Input model
class ContentInput(BaseModel):
    text: str

# Scoring function (simple demo version)
def compute_score(text: str) -> float:
    # Placeholder: Replace with your real model logic
    score = len(text) % 100 / 100
    return round(score, 3)

@app.post("/score")
def score_content(payload: ContentInput):
    try:
        result = compute_score(payload.text)
        return {"score": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Local run (ignored online)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
