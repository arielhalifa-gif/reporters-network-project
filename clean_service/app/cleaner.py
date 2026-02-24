import re

STOP_WORDS = {"the", "and", "is", "in", "to", "of"}

def clean_text(text: str) -> str:

    # lowercase
    text = text.lower()

    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # remove stop words
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]

    return " ".join(words)