def compute_metrics(text: str) -> dict:

    words = text.split()

    word_count = len(words)
    char_count = len(text)
    unique_words = len(set(words))

    avg_word_length = (
        sum(len(w) for w in words) / word_count
        if word_count > 0 else 0
    )

    return {
        "word_count": word_count,
        "char_count": char_count,
        "unique_words": unique_words,
        "avg_word_length": round(avg_word_length, 2)
    }