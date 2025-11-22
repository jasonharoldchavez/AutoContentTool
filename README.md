# AutoContentTool

AutoContentTool is a lightweight FastAPI-based backend that generates structured content using AI-assisted logic.  
It provides a simple `/generate` endpoint that accepts text input and returns enhanced structured output.

## Features

- FastAPI backend
- Clean input/output validation
- Extendable content generation logic
- Ready for deployment or expansion

## Endpoints

### `POST /generate`

**Request body:**
```json
{
  "text": "Your input text"
}{
  "original": "...",
  "generated": "..."
}pip install -r requirements.txtuvicorn app:app --reloadhttp://127.0.0.1:80004.
