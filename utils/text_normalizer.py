import re


def strip_mentions_and_whitespace(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\[([^\]]+)]\(mention:[^)]+\)", "", text)
    text = re.sub(r"@\S+", "", text)
    text = re.sub(r":\w+:", "", text)
    text = text.replace("—", "-").replace("–", "-")
    text = re.sub(r"\s+", " ", text)
    return text.strip()
