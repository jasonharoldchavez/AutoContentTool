def sanitize_text(text: str) -> str:
    """
    Removes problematic whitespace and ensures clean input.
    Add more sanitization rules here if needed.
    """
    return text.strip()

def ensure_min_length(text: str, min_len: int = 1) -> bool:
    """
    Checks whether the input meets a minimum length requirement.
    """
    return len(text) >= min_len
