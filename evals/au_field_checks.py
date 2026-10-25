"""Checks the Australian field notes and the home-state prompt. No model and no network.

Usage: python3 evals/au_field_checks.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from core import HOME_NO_LINE, HOME_STATES, home_clause  # noqa: E402

SEED = os.path.join(ROOT, "library", "seed")
PREVIEW_STATES = os.path.normpath(os.path.join(ROOT, "..", "src", "content", "states.ts"))

# Question, note that should answer it, regexes that note must satisfy.
QUESTIONS = [
    ("The street power is out. Will my normal grid-tied rooftop solar run the fridge?",
     "grid.md", [r"produces nothing", r"shut down", r"backup"]),
    ("A bluebottle stung my leg. Do I use vinegar and the snake pressure bandage?",
     "marine.md", [r"Do not pour vinegar", r"45", r"20 minutes", r"wrong treatment"]),
    ("How many drops of bleach go in a jerry can of creek water?",
     "water.md", [r"[Dd]o not copy a US bleach", r"[Bb]oil"]),
    ("Is this berry edible?",
     "bush.md", [r"Do not forage"]),
]


def read(name):
    with open(os.path.join(SEED, name), encoding="utf-8") as f:
        return f.read()


def main():
    failed = 0
    for question, name, patterns in QUESTIONS:
        text = read(name)
        for pattern in patterns:
            if not re.search(pattern, text):
                failed += 1
                print(f"FAIL  {name} missing /{pattern}/")
                print(f"      {question}")
    notes = read("emergency-numbers.md")
    for code, (_name, number, _what) in HOME_STATES.items():
        if number not in notes:
            failed += 1
            print(f"FAIL  emergency-numbers.md does not list {code} {number}")
        clause = home_clause(code)
        if number not in clause or "132 500" not in clause:
            failed += 1
            print(f"FAIL  home clause for {code} lost its own number")
        for other, other_number, _w in HOME_STATES.values():
            if other_number != number and other_number in clause:
                failed += 1
                print(f"FAIL  {code} clause also contains {other_number}")
    for code in HOME_NO_LINE:
        clause = home_clause(code)
        if "no fire-information" not in clause or "Do not borrow" not in clause:
            failed += 1
            print(f"FAIL  {code} should refuse a borrowed fire line")
    if "1800 679 737" in home_clause("VIC"):
        failed += 1
        print("FAIL  Victoria was given the NSW fire line")
    rules_bits = [
        ("grid.md", "Microinverter"),
        ("marine.md", "blue-ringed"),
        ("asthma.md", "four separate puffs"),
        ("radio.md", "channels **5** and **35**"),
        ("quake.md", "Drop, cover, and hold"),
        ("sanitation.md", "30 metres"),
        ("smoke.md", "evaporative"),
        ("cold.md", "carbon monoxide"),
        ("trees.md", "10 metres"),
        ("plan.md", "RediPlan"),
        ("mosquitoes.md", "Ross River"),
    ]
    for name, needle in rules_bits:
        if needle not in read(name):
            failed += 1
            print(f"FAIL  {name} lost {needle!r}")
    if os.path.exists(PREVIEW_STATES):
        preview = open(PREVIEW_STATES, encoding="utf-8").read()
        for _code, (_name, number, _what) in HOME_STATES.items():
            if number not in preview:
                failed += 1
                print(f"FAIL  preview states.ts missing {number}")
    else:
        failed += 1
        print("FAIL  preview states.ts not found")
    if failed:
        print(f"{failed} failed")
        sys.exit(1)
    print(f"ok  {len(QUESTIONS)} questions, {len(HOME_STATES)} state lines, {len(HOME_NO_LINE)} refusals")


if __name__ == "__main__":
    main()
