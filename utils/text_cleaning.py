def basic_text_cleaning(text):
    text = text.replace("\n", " ").replace("\\n", " ").replace("\r", " ").replace("\\", " ")
    
    text = text.replace(","," ").replace("&", "and").replace('""', '')
    
    text = text.lower()
    
    return text.strip()
