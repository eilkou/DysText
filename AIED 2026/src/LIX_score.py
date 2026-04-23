#!/usr/bin/env python3
# LIX_score.py
#
# Returns True if LIX(new_chapter) < LIX(old_chapter)
# (lower LIX = more readable)

import re


def lix(text):
    words = re.findall(r"\b\w+\b", text)
    sentences = re.split(r"[.!?]+", text)

    if not words or not sentences:
        return float("inf")

    long_words = [w for w in words if len(w) > 6]

    return (
        len(words) / max(len(sentences), 1)
        + (len(long_words) * 100 / len(words))
    )


def failed_score(new_chapter, old_chapter):
    print("LIX new",lix(new_chapter))
    print("LIX old",lix(old_chapter))
    # The best the readability, the lower the LIX score
    # Error is set to 2 
    return lix(new_chapter) > lix(old_chapter)
    
def get_instructions(text: str) -> str:
    """
    Returns an instruction string. If LIX is already <= target, returns a light constraint
    to keep readability stable.
    """
    score = lix(text)
    target_lix = 45.0
    instructions="Improve readability; avoid long sentences, and prefer common words."
    failed='LIX'

    if score > target_lix:
        return instructions, failed
    else:
        return '',''

