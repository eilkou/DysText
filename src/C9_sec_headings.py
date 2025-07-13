import re

def detect_headings(text):

    heading_pattern = re.compile(
    r'^(?:\#{1,6}\s*.+|\*\*.+\*\*|\d+\)\s+[A-Z][^\n]*)', re.MULTILINE
)

    # Search for section headings
    headings = heading_pattern.findall(text)

    has_headings = len(headings) > 0

    return has_headings, headings


def C9_score(text):
    has_headings, headings = detect_headings_and_toc(text)
    score=0
    if has_headings:
        print("------------------- HEADINGS --------------------")
        print("The headings are: ", headings)
        score=score+1

    return score


