import re

def detect_bullet_points(text):
    # Use regex to detect the literal string '\n*'
    pattern = r"\n\*|\n-|\n   -"
    matches = re.findall(pattern, text)
    return matches


def C13_score(text):
    if len(detect_bullet_points(text))>0:
        return 1
    return 0

