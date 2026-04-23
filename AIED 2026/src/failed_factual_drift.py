#!/usr/bin/env python3
# failed_factual_drift.py
#
# True  => likely factual drift (entities or numbers lost too much)
# False => looks stable
#
# Uses spaCy NER if available; otherwise falls back to a simple heuristic.

import re

NUMBER_RE = re.compile(r"\b\d+(?:[.,]\d+)?\b")


def extract_numbers(text: str) -> set[str]:
    return set(NUMBER_RE.findall(text or ""))


def overlap_recall(old_set: set[str], new_set: set[str]) -> float:
    """Recall of old items preserved in new."""
    if not old_set and not new_set:
        return 1.0
    if not old_set:
        return 1.0
    if not new_set:
        return 0.0
    return len(old_set & new_set) / len(old_set)


def _heuristic_entities(text: str) -> set[str]:
    # Fallback heuristic: sequences of capitalized words, plus ALLCAPS acronyms
    caps_seq = re.findall(r"\b(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b", text or "")
    acronyms = re.findall(r"\b[A-Z]{2,}\b", text or "")
    return {s.strip() for s in caps_seq + acronyms if s.strip()}


def extract_entities(text: str) -> set[str]:
    """
    Prefer spaCy NER if installed + model available.
    Otherwise fallback to heuristic.
    """
    try:
        import spacy  # type: ignore
        try:
            nlp = spacy.load("en_core_web_sm")
        except Exception:
            # spaCy installed but model missing
            return _heuristic_entities(text)

        doc = nlp(text or "")
        ents = set()
        for ent in doc.ents:
            # Keep common "factual" entity types; tune as needed
            if ent.label_ in {
                "PERSON", "ORG", "GPE", "LOC", "PRODUCT",
                "EVENT", "WORK_OF_ART", "LAW", "NORP",
                "FAC", "LANGUAGE", "DATE", "TIME", "PERCENT", "MONEY", "ORDINAL"
            }:
                ents.add(ent.text.strip())
        return {e for e in ents if e}
    except Exception:
        # spaCy not installed (or other import/runtime issue)
        return _heuristic_entities(text)


def failed_factual_drift(
    new_text: str,
    old_text: str,
    min_entity_recall: float = 0.50,  # preserve >=50% of old entities
    min_number_recall: float = 0.75,  # preserve >=75% of old numbers
) -> bool:
    old_ent = extract_entities(old_text)
    new_ent = extract_entities(new_text)
    old_num = extract_numbers(old_text)
    new_num = extract_numbers(new_text)

    ent_recall = overlap_recall(old_ent, new_ent)
    num_recall = overlap_recall(old_num, new_num)
    #print("Entity recall",ent_recall)
    #print("Num_recall", num_recall)
    
    entity_drift = ent_recall < min_entity_recall
    number_drift = num_recall < min_number_recall

    return entity_drift or number_drift



