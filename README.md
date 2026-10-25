# Australian Survival LLM

An Australian fork of [survival-llm](https://github.com/anonnerdfrenzy/survival-llm) by Ronny Fernandez.
The local app is unchanged in shape: Ollama on your computer, a SQLite FTS5 library, answers that cite the passage they used, and a **Your files** folder for PDFs you have a right to hold. Nothing in the question path needs the network once the library and the model are installed.

This fork drops US emergency sources that do not travel (Ready.gov, CDC travellers' pages, MedlinePlus, US military survival and first-aid manuals, USDA canning, US micromort tables). It adds Australian field notes — bushfire and smoke, flood, cyclone, heat, earthquake, snakebite, marine stings, asthma, a dead grid-tied solar array, radio and beacons — and a fetch path for CC BY Australian pages, including Geoscience Australia. Official PDFs that are free to read but not free to republish are **not** copied into the repo. [AUSTRALIAN_SOURCES.md](AUSTRALIAN_SOURCES.md) says where to get them and how to drop them in Your files. The local app has a home-state setting so a fire-information number from one state is not offered for another.

Code: MIT ([LICENSE](LICENSE)), same as upstream. Field notes: CC BY 4.0. Every other article keeps its own licence ([SOURCES.md](SOURCES.md)).

The model is not an ambulance. In Australia call **000**. Storm and flood damage: **132 500**. Poisons: **13 11 26**.

## What changed from upstream

- `library/fetch_zims.py` no longer asks for Ready.gov, CDC, MedlinePlus, USDA canning, US military medicine, or the mixed-rights zimgit bundles.
- `library/fetch_manuals.py` does not download the US manual set. Open manuals are the default list (empty until a PDF is cleared). `--nc` fetches IFRC/WHO. `--personal` fetches pico-hydro and related guides for a library you do not publish.
- `library/fetch_risk.py` refuses the US mortality downloads.
- `library/fetch_au.py` fetches YourHome and FSANZ pages when the site returns real text. Both are CC BY 4.0.
- `library/seed/` is indexed on every build as "Australian field notes".
- `library/search.py` ranks those notes and Australian open pages above wikis, and does not badge the notes as a government publisher.
- `core.py` speaks Australian English, calls 000 rather than 911, and prefers Australian notes over US first-aid habits on snakes and spiders.
- Model choice by RAM is unchanged (Granite around 16 GB, Qwen around 32 GB and up, Nemotron when the machine is large). See the table below. It is a reasonable fit for a home computer with 16–32 GB, and the bigger models want more.

## Install

Do this while you have internet. After that, the app needs none. Setup takes 20 minutes to about 2½ hours, depending on
your computer and internet speed (the biggest AI model is 80 GB); you only click for about 5 minutes.

**Mac** (Apple Silicon, macOS 14 Sonoma or newer)
1. Download `Survival-LLM-mac.zip` and double-click it to unzip. Move **Australian Survival LLM** to Applications if you like.
2. Double-click **Australian Survival LLM**. The first time, macOS says it can't verify the app, because it isn't sold through
   Apple. Click **Done**, open **System Settings > Privacy & Security**, scroll down to "Australian Survival LLM was blocked",
   click **Open Anyway**, and confirm with your password. You only do this once.

**Windows** (10 or 11, 64-bit)
1. Download `Survival-LLM-windows.zip`, right-click it and choose **Extract All**. (Running it from inside the zip doesn't work.)
2. Open the extracted **Australian Survival LLM** folder and double-click **Australian Survival LLM.bat**. If Windows says it protected
   your PC, click **More info**, then **Run anyway**.

**Then** the app opens in its own window and walks you through setup:
1. **AI engine:** built into the Mac app. On Windows, one click downloads it (Ollama, 1.6 GB).
2. **AI model:** it suggests the best one for your computer's memory (below) and downloads it.
3. **Library:** "Everything" (8.8 GB download) or "Essentials" (1.3 GB, without Wikipedia and iFixit).

**Free disk space needed:** the model's size plus 5 GB, plus about 27 GB while the full library installs
(21 GB once installed), or about 10 GB for Essentials (3 GB once installed).

## Uninstall

Delete the app, then these folders: the AI models, in `~/.ollama/models` (shared with any other Ollama on the
computer, so keep it if you use Ollama elsewhere), and the library, in `~/Australian Survival LLM Library`. Your own files are in
`~/Australian Survival LLM Files`; keep that folder if you want them. The app's own
settings are in `~/Library/Application Support/Australian Survival LLM` on a Mac, and in `%APPDATA%\Australian Survival LLM` plus the
AI engine in `%LOCALAPPDATA%\Australian Survival LLM` on Windows.

## Which model your computer gets

The app checks your memory and suggests a model. More memory, smarter model.

| Your computer | Model | Download |
|---|---|---|
| Mac with 128 GB or more | NVIDIA Nemotron 3.5 Super (`nemotron-3.5-super:120b-a12b-nvfp4`) | 80 GB |
| Mac with 32-96 GB | Qwen3.8 27B (`qwen3.8:27b-mlx`) | 18 GB |
| Windows PC with 32 GB or more | NVIDIA Nemotron 3.5 Lightning (`nemotron-3.5-lightning:30b-a3b`) | 25 GB |
| Mac or PC with 16-31 GB | IBM Granite 4.2 8B (`granite4.2:8b`) | 6 GB |

Nemotron Super needs 128 GB because macOS lets the graphics side use only about three quarters of memory.

Gemma 4 E4B (`gemma4`, 10 GB) is offered as a faster option for 16 GB computers. Computers with 8 GB can
still search the library; no model we tested was both small enough and safe enough to recommend for them.

## How the models did (upstream, not this fork)

These scores are from the original survival-llm library in October 2026, judged against USDA, CDC, FEMA and
similar US guidance. They are a comparison of models, not a test of the Australian notes. Do not treat them
as a safety claim for this fork. Re-run `evals/` against a library you built here before you quote a number.

How these numbers were measured, plainly: the tests ran on an earlier build of the library, before Wikipedia
was added, which also held some material that isn't in the public downloads (the Kiwix "zimgit" collections and
MedlinePlus's licensed encyclopedia and drug pages; 1 to 10 answers per model read one of those). The app's
instructions have also gained rules since: the carbon monoxide rule and "always give your best estimate". Treat
the table as a comparison between models, not a guarantee for the version you download.

| Model | Accuracy | Main point right | Harmful answers | Seconds per answer* |
|---|---|---|---|---|
| Nemotron 3.5 Super | 86% | 21 of 22 | 0 | 12 |
| Qwen3.8 27B | 80% | 21 of 22 | 0 | 40 |
| Nemotron 3.5 Lightning | 77% | 19 of 22 | 1 | 8 |
| Qwen 3.6 (36B MoE) | 59% | 15 of 22 | 1 | 24 |
| Granite 4.2 8B | 55% | 14 of 22 | 0 | 29 |
| Granite 4.2 30B | 55% | 11 of 22 | 2 | 55 |
| Gemma 4 E4B | 48% | 11 of 22 | 0 | 3 |
| Granite 4.2 3B | 44% | 8 of 22 | 5 (2 could kill) | 12 |

\* On an M4 Max MacBook Pro (128 GB), Ollama 0.40.9. Qwen3.8 27B was tested as mlx-community's 4-bit build
(`local-ai2` in `evals/results`); the app downloads Ollama's NVFP4 build of the same model. Nemotron Super appears
there as `local-ai1` (the same model with the app's settings). Windows downloads a different file of Nemotron
Lightning (Q4_K_M) than the Mac build tested here. Accuracy is the share of points on a 0-3 scale per answer; "harmful"
means following it could hurt someone. Granite 4.2 3B, first planned for 8 GB computers, is not offered: it
told people not to use a tourniquet on an arm and to stay 3 feet from a downed power line (the guidance is 35).
Qwen 3.6 is not offered either: it got stuck repeating itself on two questions (once for 94 minutes),
which is also why answers have a length limit (you can change it, or turn it off, next to Send).

The tests found and fixed two problems for every model: some kept looking things up until they ran out of
lookups and never answered (now they are told to answer from what they read), and several gave "if you
must" exceptions for running cars and generators near the house (the prompt now rules those out).
Reproduce with `evals/retrieval_eval.py`, `evals/make_judging_batches.py` and `evals/score_judging.py`;
answers are in `evals/results/`, grades in `evals/judging/`.

**Made-up sources.** Each answer ends with the model's own "Sources:" line, and its instructions say the app shows
every article it opened. Models name sources they never saw anyway. In a separate test of 14 questions
(`evals/citation_check.py`, October 24 2026), these answers named a source the model had neither opened nor seen in
its search results: Nemotron Super 6 (mostly answering from memory and naming Ready.gov or the CDC), Lightning 3,
Gemma 3, Granite 2 and Qwen3.8 27B 1. So the app checks that line against what the model opened or saw, and replaces
a line that names anything else with the list of articles it actually read.

## How it works

```
your question ─► local model (Ollama) ─► search_library ─► SQLite full-text index ─► passages
                        ▲                read_article  ─► plain-text library files
                        └──── answer with "Sources:" ◄──┘   show_article ─► opens it on screen
```

- `app/server.py` serves the chat page on `127.0.0.1` only and runs each turn through `core.py`.
- `core.py` streams the model's answer and runs its three tools: `search_library`, `read_article`, `show_article`.
- `library/search.py` searches `index.sqlite` (FTS5, BM25 ranking over ~1,500-character passages, official sources ranked higher) and reads the plain-text Markdown shards.
- `library/myfiles.py` reads the person's own files into a small index of their own (kept with the app's settings) and searches it together with the library.
- Everything except Ollama, the app window (pywebview) and PDF reading (pypdf) is the Python standard library.

## Run from source

```bash
python3 app/server.py          # the app in its own window (needs `pip install pywebview pypdf`; else it uses your browser)
python3 app/server.py --browser                     # in your web browser instead
python3 chat.py "How long is fridge food safe in a blackout?"   # terminal; --model NAME picks a model
```

The library is looked up at `$SURVIVAL_LLM_LIBRARY`, then `~/Australian Survival LLM Library`, then `library.noindex/` next to the code.
Without a built-in engine, the app uses an Ollama you have installed (`ollama serve`).

## Build the library

```bash
python3 -m venv .venv && .venv/bin/pip install libzim lxml trafilatura
python3 library/fetch_au.py          # YourHome and FSANZ, CC BY, skipped if the page is empty
python3 library/fetch_zims.py        # Wikipedia, WikEM, Appropedia, Energypedia and the other open wikis
python3 library/fetch_manuals.py     # prints the licence gate; add --nc or --personal if you mean to
python3 library/build_library.py     # field notes + whatever open downloads landed in library.noindex/
```

A useful index exists after `build_library.py` even if you skip the ZIM downloads. The seed notes are in the repo.

Selected wikiHow is non-commercial. Fetch the CSV and pass `--with-nc` if you want it in a personal library:

```bash
curl -L -o library.noindex/raw/wikihowAll.csv \
  https://huggingface.co/datasets/Lajvi/wikihowAll/resolve/main/wikihowAll.csv
.venv/bin/python library/build_library.py --with-nc
```

`build_library.py` is incremental (finished sources are skipped) and `--rebuild KEY ...` redoes sources.
It needs `pdftotext` (poppler) for PDF manuals. After you add a source, say so in SOURCES.md and rebuild that key.

**A default build is the shareable Australian set** (field notes, CC BY pages, CC BY-SA wikis, OGL medicines).
`--public` is the same idea, written to another folder. `--lite` leaves out the big Wikipedia dump.
`--with-nc` and `--personal` are for your own machine. Do not publish those libraries.

```bash
LIBRARY_OUT=dist/library-full .venv/bin/python library/build_library.py --public
LIBRARY_OUT=dist/library-lite .venv/bin/python library/build_library.py --lite
python3 packaging/make_packs.py --base-url https://github.com/HowMuchCanAKoalaBare/australian-survival-llm/releases/download/vX.Y.Z \
  lite=dist/library-lite full=dist/library-full
```

Packs carry a date (`--version`, default today); installed copies offer a pack with a newer date as an update.

## Package the apps

```bash
packaging/build.sh     # dist/Survival-LLM-mac.zip and dist/Survival-LLM-windows.zip (needs Xcode's command-line tools)
gh release create "v$(cat packaging/VERSION)" dist/Survival-LLM-mac.zip dist/Survival-LLM-windows.zip
python3 packaging/make_update.py "What's new" "..."   # writes docs/update.json; publish docs/ afterwards
```

Set the version in `packaging/VERSION` first. Installed copies read `docs/update.json` from the project's web page,
download the zip for their system, check its size and SHA-256, and replace themselves with it.

The Mac app bundles a portable Python, pywebview for its window, and Ollama. The Windows app bundles Python and
pywebview and downloads Ollama on first use (it is 1.6 GB with its graphics-card libraries).

## License

Code: MIT ([LICENSE](LICENSE)). Library content keeps the license of its source ([SOURCES.md](SOURCES.md)).

AI models make mistakes. Every answer shows its sources so you can check.
