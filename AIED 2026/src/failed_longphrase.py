#!/usr/bin/env python3
# failed_longphrase.py
#
#   true  -> if any phrase has more than 45 words
#   false -> otherwise

import json
import re
import sys

# max threshold of a sentence containing nonsense
MAX_WORDS = 45


def failed_longphrase(text):
    # Split on sentence/phrase boundaries
    phrases = re.split(r"[.!?\n]+", text)

    for p in phrases:
        words = re.findall(r"\b[\w']+\b", p)
        print("phrase", p)
        print("words",words)
        if len(words) > MAX_WORDS:
            return True
    return False


