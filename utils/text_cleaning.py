def basic_text_cleaning(text):
    text = text.replace("\n", " ").replace("\\n", " ").replace("\r", " ").replace("\\", " ").strip()
    return text
