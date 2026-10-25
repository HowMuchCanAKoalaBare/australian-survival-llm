# Evaluations

The JSONL files in `results/` and the judging notes in `judging/` are the upstream survival-llm runs from October 2026.
They used a US-heavy library and US official guidance (USDA, CDC, FEMA). They are kept so the model table in the README has a source. They are not scores for this fork.

`citation_check.py` questions have been edited toward Australian prompts (snakebite, 13 11 26, creek power). Re-run them after you build a library.

`au_field_checks.py` does not need Ollama. It checks four failure modes against the field notes (grid-tied solar in a blackout, bluebottle versus a snake bandage, no invented bleach dose, no edible berry) and checks that a home state is not given another state's fire-information number. Queensland, the ACT and the Northern Territory are refusals: the library does not carry a fire-information number for them.
