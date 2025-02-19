import re

def check_extra_space(text):
    # Split the input text into lines
    lines = text.split('\n')

    # Keep track of previous line type: heading or paragraph
    previous_line_was_heading = False
    extra_space_found = False

    # Loop through the lines to detect extra spaces between headings and paragraphs
    for i in range(len(lines) - 1):
        current_line = lines[i].strip()
        next_line = lines[i + 1].strip()

        # Check if the current line is a heading (simple check for lines starting with # or all caps)
        if re.match(r'^[#\*]{1,6}\s', current_line) or current_line.isupper():
            previous_line_was_heading = True
        elif current_line:  # Non-empty line, presumably a paragraph
            if previous_line_was_heading and not next_line:
                # If we have a heading followed by an empty line, check if there's more than one blank line
                if i + 2 < len(lines) and not lines[i + 2].strip():
                    extra_space_found = True
            previous_line_was_heading = False

    return extra_space_found


def C17_score(text):
    if check_extra_space(text):
        return 1
    return 0
#
# # Example usage:
# text = """
# Soil erosion is not a general problem in West Africa under indigenous husbandry systems. It
# is, however, locally a chronic problem, and in many areas a potential hazard under changing
# cultivation practices. Soil erosion is intimately associated with problems of water control
# and desertification, and it is thus convenient to consider both together.
#
#
# Furthermore, over much of this area the rainfall is unreliable in amount and occurrence,
# both seasonally and annually. Also it is commonly very intense. Thus conservation measures
# must involve efficient use of the available moisture, and the prevention of the adverse
# effect of intense rainfall, such as flash floods. A special section has been created in this
# chapter to discuss the drought at the Sahel region.
#
# Maintaining a plant cover and mulching, separately or together, constitute one approach to
# the problem, but the preservation of useless plants simply as a conservation measure
# involves the waste of moisture which might otherwise go the crop plant, and is feasible only
# in areas where the water supply is more or less adequate to the being grown.
#
# # io
#
# Some more text here after the heading.
#
#
#
# Some more text after the second heading.
#
#
# """
# result = C17_score(text)
# print(result)  # This should return True if extra whitespace is found around headings or between paragraphs
