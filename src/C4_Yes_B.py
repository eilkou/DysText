import re

def detect_text_formatting(text):

    bold_pattern = r'(\*\*(.*?)\*\*|<bold>(.*?)</bold>)'  # Bold in Markdown or LaTeX

    bold_matches = re.findall(bold_pattern, text)

    bold_count = len(bold_matches)

    return  bold_count

def C4_score(text):
    bold_count = detect_text_formatting(text)
    score=0
    if bold_count>0:
        score=score+1
    return score


