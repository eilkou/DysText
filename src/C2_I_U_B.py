import re

def detect_text_formatting(text):
    """
    Detects bold, italics, and underline formatting in the text and returns the count for each.
    - Avoid words surrounded by __ or * (italics and underline).
    - Score 1 for words surrounded by ** (bold) or <bold> (LaTeX-like bold).

    :param text: The input text to analyze.
    :return: A dictionary containing:
        - "Italics Count": The number of italics occurrences.
        - "Underline Count": The number of underline occurrences.
        - "Bold Count": The number of bold occurrences.
        - "Score": 1 if bold formatting is found, otherwise 0.
    """
    # Regex patterns to detect the formatting types
    bold_pattern = r'(\*\*(.*?)\*\*|<bold>(.*?)</bold>)'  # Bold in Markdown or LaTeX
    italics_pattern = r'(\*(.*?)\*|_(.*?)_)'  # Italics or underline
    underline_pattern = r'__(.*?)__'  # Underlined in Markdown

    # Find all bold, italics, and underline patterns
    bold_matches = re.findall(bold_pattern, text)
    italics_matches = re.findall(italics_pattern, text)
    underline_matches = re.findall(underline_pattern, text)

    # Count of occurrences for each formatting type
    bold_count = len(bold_matches)
    italics_count = len(italics_matches)
    underline_count = len(underline_matches)

    # Score of 1 if any bold formatting is found, otherwise 0
    score = 1 if bold_count > 0 else 0

    return italics_count, underline_count, bold_count

    # return {
    #     "Italics Count": italics_count,
    #     "Underline Count": underline_count,
    #     "Bold Count": bold_count,
    #     "Score": score
    # }


# # Example usage:
# text = "This is a test with __underline__ and *italics* and **bold** words. Also, <bold>latex bold</bold>."
#
# result = detect_text_formatting(text)
# print(result)

def C2_score(text):
    italics_count, underline_count, bold_count = detect_text_formatting(text)
    score=0
    if italics_count>0:
        score=score-1
    if underline_count>0:
        score=score-1
    if bold_count>0:
        score=score+1
    return score

# print(C2_score(text))
