#!/usr/bin/env python3
# agent.py
#
# Logs per-iteration results to ONE common CSV:
#   - iteration
#   - failed checks (from checker)
#   - LIX + DysText scores (only if it reaches judge)
#
# Assumptions:
# - prompter(chapter, instructions) exists
# - checker(new_chapter, old_chapter) returns (passed, instructions, failed_checks_list)
# - LIX_score.py exposes lix(text) and get_instructions(text)
# - DysText_score.py exposes score(text) and get_instructions(text)
# - judge(new_chapter) exists and returns instruction string (no LLM call)

import csv
import hashlib
import json
import os
from typing import Any, Dict, List, Tuple

from prompter import prompter
from checker import checker
from judge import judge

import LIX_score
import DysText_score

MAX_PASSES = 3
CSV_PATH = "agent_log.csv"


def chapter_key(original_text: str) -> str:
    return hashlib.sha256((original_text or "").encode("utf-8")).hexdigest()


def append_row(path: str, header: list[str], row: dict):
    new_file = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        if new_file:
            w.writeheader()
        w.writerow(row)


def process_chapter(original_chapter: str, meta: dict) -> str:
    key = chapter_key(original_chapter)

    current_chapter = original_chapter
    instructions = (
        "Rewrite this chapter to be more readable and dyslexia-accessible. "
        "Keep all facts and meaning. Use clear, short sentences."
    )

    header = [
        "chapter_key",
        "iteration",
        "failed_checks",
        "reached_judge",
        "lix_score",
        "dystext_score",
    ]

    for iteration in range(1, MAX_PASSES + 1):
        # 1) LLM pass
        new_chapter = prompter(current_chapter, instructions)

        # 2) Hard checks
        passed, next_instructions, failed_checks = checker(
            new_chapter=new_chapter,
            old_chapter=original_chapter,   # compare drift to the true original
        )

        reached_judge = False
        lix_score = ""
        dystext_score = ""

        # 3) If passed, compute scores (judge stage reached)
        if passed:
            reached_judge = True
            lix_score = LIX_score.lix(new_chapter)

            # DysText_score.score can be numeric or dict; store compactly
            ds = DysText_score.score(new_chapter)
            if isinstance(ds, (int, float)):
                dystext_score = ds
            else:
                # if dict/list/bool/etc, store as string so CSV remains valid
                dystext_score = str(ds)

            # judge generates next instructions (no LLM call)
            judge_instructions = judge(new_chapter)
            instructions = judge_instructions if judge_instructions.strip() else ""
        else:
            # checker failed: feed instructions into next iteration
            instructions = next_instructions

        # 4) Log ONE row for this iteration
        append_row(
            CSV_PATH,
            header,
            {
                "chapter_key": key,
                "iteration": iteration,
                "failed_checks": ",".join(failed_checks),
                "reached_judge": reached_judge,
                "lix_score": lix_score,
                "dystext_score": dystext_score,
            },
        )

        # 5) stopping conditions
        current_chapter = new_chapter

        # Early stop if it reached judge and judge had nothing to add
        if passed and not instructions:
            return new_chapter

    return current_chapter

def main(input_json: str, output_json: str):
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of chapter objects.")

    out = []
    for item in data:
        text = str(item.get("text", ""))

        rewritten = process_chapter(
            original_chapter=text,
            meta=item,
        )

        item_out = dict(item)
        item_out["rewritten_text"] = rewritten
        out.append(item_out)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Example usage:
    #   python agent.py input.json output.json
    import sys
    if len(sys.argv) != 3:
        print("Usage: python agent.py input.json output.json")
        raise SystemExit(1)

    main(sys.argv[1], sys.argv[2])
