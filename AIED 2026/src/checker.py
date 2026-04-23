#!/usr/bin/env python3
# checker.py
#
# Runs hard checks and returns (passed, instructions_for_next_iteration).
# Includes:
#   - failed_longphrase
#   - failed_factual_drift

from failed_longphrase import failed_longphrase
from failed_factual_drift import failed_factual_drift


def checker(new_chapter, old_chapter):
    instructions = []
    failed = []

    # 1) Long phrase / gibberish risk
    if failed_longphrase(new_chapter):
        instructions.append(
            "Do NOT produce gibberish. This is an educational task."
        )
        failed.append("longphrase")

    # 2) Factual drift (entities / numbers changed too much)
    if failed_factual_drift(new_chapter, old_chapter):
        failed.append("factual_drift")
        instructions.append(
            "Rewrite again while STRICTLY preserving key entities and numbers/dates from the original. "
            "Do not add new facts."
        )

    # If any hard check failed, return combined corrective instructions for next iteration
    if instructions:
        return False, "\n".join(instructions).strip(), failed

    # Otherwise pass
    return True, "", failed

