import re

# C13: Detect Section headings & ToC
def detect_headings_and_toc(text):
    # Regular expression for detecting headings
    # heading_pattern = re.compile(r'^[A-Z][A-Za-z0-9\s\-:]+(?:\n|\r|$)', re.MULTILINE)
     # We will extract only the text inside '**' (ignoring the bold markers)
    heading_pattern = re.compile(
    r'^(?:\#{1,6}\s*.+|\*\*.+\*\*|\d+\)\s+[A-Z][^\n]*)', re.MULTILINE
)


    # Try to detect a Table of Contents (common structure)
    toc_pattern = re.compile(r'(?:table of contents|contents)(.*?)(?=\n|$)', re.IGNORECASE | re.DOTALL)

    # Search for section headings
    headings = heading_pattern.findall(text)

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

    has_headings = len(headings) > 0

    return has_headings, headings, has_toc, toc_entries

#
# sample_text = """
#     Table of Contents
#     -----------------
#     Introduction  1
#     Chapter 1     2
#     Chapter 2     5
#     Conclusion    10
#
#     Introduction
#     -------------
#     This is the introduction.
#
#     Chapter 1:
#
#      **Technical Support:**
#
#     ---------
#     This is the first chapter.
#
#     Chapter 2
#     ---------
#     This is the second chapter.
#
#     Conclusion
#     ----------
#     This is the conclusion.
#     """
#
# # Detect headings and TOC
# has_headings, headings, has_toc, toc = detect_headings_and_toc(sample_text)
#
#
# # Output results
# print(f"Has Headings: {has_headings}")
# print(f"Headings: {headings}")
# print(f"Has Table of Contents: {has_toc}")
# print(f"Table of Contents: {toc}")

def C7_score(text):
    has_headings, headings, has_toc, toc = detect_headings_and_toc(text)
    score=0
    if has_headings:
        print("------------------- HEADINGS --------------------")
        print("The headings are: ", headings)
        score=score+1
    if has_toc:
        print("------------------- TABLE OF CONTENT --------------------")
        print("The Table of Content is:", toc)
        score=score+1
    return score

# print(C7_score(sample_text))
