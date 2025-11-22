from .utils import sanitize_text, ensure_min_length

def generate_auto_content(text: str) -> str:
    """
    Core content generation logic.
    This is where you can later plug in AI models, APIs, or custom rules.
    """

    cleaned = sanitize_text(text)

    if not ensure_min_length(cleaned, min_len=1):
        return "Error: Input text is too short."

    processed = cleaned.capitalize()

    return f"Auto-Generated Content: {processed}"
