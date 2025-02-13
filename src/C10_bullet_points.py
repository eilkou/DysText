import re

def detect_bullet_points(text):
    # Use regex to detect the literal string '\n*'
    pattern = r"\n\*|\n-|\n   -"
    matches = re.findall(pattern, text)
    return matches

# # Example usage:
# text = """Please provide me with a question so I can give you an answer in bullet points! 😊  \n\nFor example, you could ask: \n\n* What are the benefits of exercise?\n* What are the main ingredients in a cake?\n* How do I change a tire? \n\n\nLet me know what you'd like to learn about! 🚀 \n"""
#
# matches = detect_bullet_points(text)
# print(f"Bullet points found: {len(matches)}")

def C10_score(text):
    if len(detect_bullet_points(text))>0:
        return 1
    return 0

# print(C10_score(text))
