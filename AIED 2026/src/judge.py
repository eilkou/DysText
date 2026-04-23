#!/usr/bin/env python3
# judge.py
#
# Takes the new chapter text, gathers instructions from:
#   - DysText_score.py
#   - LIX_score.py

from DysText_score import get_instructions as dystext_instructions
from LIX_score import get_instructions as lix_instructions


def judge(new_chapter):
    lix_in,lix_failed=lix_instructions(new_chapter)
    dystext_in, dystext_failed=dystext_instructions(new_chapter)

    # Failed criteria in accessibility
    failed = []

    # Instructions for improving text
    instructions = []

    if isinstance(dystext_in, list):
        instructions.extend(dystext_in)
    elif dystext_in:
        instructions.append(dystext_in)

    if lix_in:
        instructions.append(lix_in)
        
    # LIX
    if isinstance(lix_failed, list):
        failed.extend(lix_failed)

    # DysText
    if isinstance(dystext_failed, list):
        failed.extend(dystext_failed)

    return "\n".join(instructions),failed
