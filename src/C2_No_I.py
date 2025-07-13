import re

def detect_text_formatting(text):

    italics_pattern = r'(\*(.*?)\*|_(.*?)_)'

    italics_matches = re.findall(italics_pattern, text)

    italics_count = len(italics_matches)

    return italics_count



def C2_score(text):
    italics_count= detect_text_formatting(text)
    score=0
    if italics_count>0:
        score=score-1
    return score


