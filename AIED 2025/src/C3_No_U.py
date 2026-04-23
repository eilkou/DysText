import re

def detect_text_formatting(text):

    underline_pattern = r'__(.*?)__'  # Underlined in Markdown
    underline_matches = re.findall(underline_pattern, text)

    underline_count = len(underline_matches)

    return underline_count



def C3_score(text):
    underline_count = detect_text_formatting(text)
    score=0
    if underline_count>0:
        score=score-1

    return score


