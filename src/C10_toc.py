import re

# C13: Detect Section headings & ToC
def detect_toc(text):

    # Try to detect a Table of Contents (common structure)
    toc_pattern = re.compile(r'(?:table of contents|contents)(.*?)(?=\n|$)', re.IGNORECASE | re.DOTALL)

    # Search for a Table of Contents section
    toc_match = toc_pattern.search(text)

    if toc_match:
        # Extract TOC content
        toc_content = toc_match.group(1)
        # Try to extract TOC entries (sections with page numbers)
        toc_entries = re.findall(r'([A-Za-z0-9\s\-]+)\s*(\d+)', toc_content)
        has_toc = True
    else:
        toc_entries = []
        has_toc = False

    return has_toc, toc_entries


def C10_score(text):
    has_toc, toc = detect_toc(text)
    score=0
    if has_toc:
        print("------------------- TABLE OF CONTENT --------------------")
        print("The Table of Content is:", toc)
        score=score+1
    return score

