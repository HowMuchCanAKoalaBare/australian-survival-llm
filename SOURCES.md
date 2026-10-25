# Library sources and licences

This is the Australian fork of [survival-llm](https://github.com/anonnerdfrenzy/survival-llm).
The code is MIT. Each source keeps its own licence, and the app shows that licence with the article.
Licences were checked on 2026-10-26. If a publisher changes its terms, trust the publisher.

The **base library** (a normal build, and any `--public` or `--lite` pack) contains only:

- public domain
- government material that is free to copy and share (Creative Commons BY, or the UK Open Government Licence)
- CC BY or CC BY-SA

It does **not** contain copyrighted commercial books, and it does not contain the US-only emergency set this fork removed.

Non-commercial sources (wikiHow, iFixit, IFRC, WHO) are optional. Build them with `--with-nc` or `--nc` on the fetch script. Do not put them in a pack you might sell.

Manuals whose licence does not allow redistribution (pico-hydro PDFs, NCAT, and anything you are unsure about) are fetched only with `--personal` and indexed only with `--personal`. Prefer Your files for those. See [AUSTRALIAN_SOURCES.md](AUSTRALIAN_SOURCES.md).

## In the base library

| Source | What it covers | Licence | Where it comes from |
|---|---|---|---|
| Australian field notes | Triple Zero, bushfire, flood, cyclone, heat, snakebite, spiders, first aid, blackout, water, food, remote travel, micro-hydro, solar | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), this project. Not an official publication | `library/seed/` |
| YourHome and FSANZ pages, when `fetch_au.py` actually receives article text | Household solar, batteries, food safety | CC BY 4.0. YourHome: Commonwealth of Australia (DCCEEW). FSANZ: Food Standards Australia New Zealand. No endorsement is implied | `library/fetch_au.py` |
| Wikipedia, most-read articles | General knowledge, including Australian topics | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), Wikipedia contributors | Kiwix `wikipedia_en_top1m` (not in `--lite`) |
| WikiMed | Medical encyclopedia drawn from Wikipedia | CC BY-SA 4.0, Wikipedia contributors | Kiwix `wikipedia_en_medicine` |
| WikEM | Emergency medicine | CC BY-SA 4.0, WikEM contributors. US-leaning in places; Australian field notes outrank it on snakes, spiders and local numbers | Kiwix `wikem_en_all` |
| Appropedia | Appropriate technology, water, sanitation, small energy | CC BY-SA 3.0 or 4.0 per page | Kiwix `appropedia_en_all` |
| Energypedia | Solar, batteries, micro-hydro, cookstoves | CC BY-SA 3.0 or 4.0 per page | Kiwix `energypedia_en_all` |
| WikiCiv | Rebuilding everyday technology | CC BY-SA 4.0 | Kiwix `wikiciv_en_all` |
| Gardenology | Plant encyclopedia. Not an Australian bush-tucker guide | CC BY-SA | Kiwix `gardenology.org_en_all` |
| UK Medicines A to Z | How common medicines are taken in the UK | UK [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Not TGA or PBS advice, and not presented as the NHS website | Kiwix `nhs.uk_en_medicines` |
| Stack Exchange: Outdoors, cooking, gardening, lifehacks, sustainable living, amateur radio, medical sciences, home improvement, mechanics, pets | Practical Q&A with the authors named on each post | CC BY-SA 2.5, 3.0 or 4.0 by post date | Kiwix Stack Exchange ZIMs |

## Optional, not in the base library

| Source | Why it is optional | How |
|---|---|---|
| Selected wikiHow articles | CC BY-NC-SA 3.0. Titles are filtered to practical how-to and away from US-only pages | Download the CSV (see README), then `build_library.py --with-nc` |
| iFixit | CC BY-NC-SA 3.0 repair guides | `fetch_zims.py` then `--with-nc` |
| IFRC first aid (2020) and WHO emergency-care and drinking-water books | Non-commercial. Not ANZCOR, and not the Australian Drinking Water Guidelines | `fetch_manuals.py --nc` then `build_library.py --with-nc` |
| Pico-hydro, NCAT/ATTRA and NRCan manuals | Free to read. Reproduction rights are missing, © NCAT, or Crown copyright you must check inside the PDF | `fetch_manuals.py --personal` then `build_library.py --personal`. Do not publish that library |

## Left out on purpose

Removed from the fetch lists and from `build_library.py`. They do not transfer to Australian conditions, or this fork will not carry them:

- Ready.gov and other FEMA preparedness pages
- CDC Travelers' Health
- MedlinePlus
- US military survival, first-aid, field sanitation, water, heat and cold manuals, and the military-medicine ZIM
- Nuclear War Survival Skills (Kearny / ORNL)
- Emergency Response Guidebook 2024 as a US DOT primary source
- USDA Complete Guide to Home Canning
- US micromort tables (SSA life tables, CDC mortality, NHTSA crashes, NWS lightning odds)
- Kiwix "zimgit" bundles (mixed rights)
- Commercial survival and bush-tucker books

Australian publications that are free to download but **not** free to republish (RediPlan, ANZCOR, AIDR handbooks, NHMRC, state fire and SES sheets) are listed in [AUSTRALIAN_SOURCES.md](AUSTRALIAN_SOURCES.md). Add your own copies through Your files.
