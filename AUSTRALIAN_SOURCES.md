# Australian and open sources

How to fill the library without breaking copyright. Checked 2026-10-26.
The base library ships original field notes (`library/seed/`) and, when you fetch them, CC BY pages and CC BY-SA wikis. Everything else below is something **you** download and keep.

## Your files (the normal way to add a PDF)

1. Run the local app (`python3 app/server.py` or `python3 app/server.py --browser`).
2. Open **Your files** and drop the PDF, or put it in the `Australian Survival LLM Files` folder in your home directory.
3. The app indexes it on that computer. It is not uploaded. A scanned page with no text layer will not be readable until you OCR it.

Do this for anything marked **Your files** in the table. Do not commit those PDFs to this repository.

## Add a source to a rebuilt library

1. Put a redistributable file where the matching fetch script expects it, or teach `library/fetch_au.py` / `library/fetch_manuals.py` the URL and the licence.
2. Confirm the licence is CC BY, CC BY-SA, public domain, or an equivalent government licence that allows sharing. If it is not, stop. Use Your files, or `--personal` for a library that never leaves your machine.
3. Rebuild: `python3 library/build_library.py --rebuild au-open` (or the source key you changed).
4. Add a row to [SOURCES.md](SOURCES.md) with the licence and the original URL.

`--public` and `--lite` refuse non-commercial sources and personal manuals. `--with-nc` adds wikiHow (filtered), iFixit, and IFRC/WHO. `--personal` adds the unclear hydro manuals. Never publish a `--personal` or `--with-nc` library as if it were the base pack.

## Emergency preparedness and first aid

| Material | Where | In the base library? |
|---|---|---|
| Australian Red Cross RediPlan and checklists | https://www.redcross.org.au/emergencies/prepare/ | No. Copyright. Your files. |
| ANZCOR / ARC guidelines (resuscitation, snakebite, anaphylaxis) | https://resus.org.au/ and https://www.anzcor.org/ | No. Free to read, not cleared to redistribute. Your files. The field notes follow the public pressure-immobilisation method and tell the model to prefer your copy. |
| AIDR Handbook Collection | https://knowledge.aidr.org.au/collections/handbook-collection/ | No. Handbooks inspected (for example Australian Emergency Management Arrangements) are CC BY-NC 4.0. Fine for you to read. Not in the public pack. Your files. |
| NSW RFS bush fire survival plan and fact sheets | https://www.rfs.nsw.gov.au/ | No, unless a named PDF states a licence that allows redistribution. Your files. |
| NSW SES flood and storm guides | https://www.ses.nsw.gov.au/ | No. Your files. |
| Other states (CFA, QFES, CFS, DFES, TAS SES, NT, ACT) | Each agency's own site | Same rule. Your files. Do not scrape the sites into the repo. |

## Water, food

| Material | Where | In the base library? |
|---|---|---|
| NHMRC Australian Drinking Water Guidelines (EH52) | https://www.nhmrc.gov.au/about-us/publications/australian-drinking-water-guidelines | No. NHMRC's notice allows personal or internal non-commercial copies, not redistribution. Your files. |
| FSANZ consumer and food-safety pages | https://www.foodstandards.gov.au/legal-policies/copyright | Yes, if `library/fetch_au.py` receives real article text. The site licence is CC BY 4.0 Australia except the logo and third-party material. Many pages are JavaScript shells; the script skips those. Save a PDF yourself if the fetch skips. |
| State health food-safety sheets | Each health department | Only when that page is clearly CC BY. Otherwise Your files. |

## Bushcraft and plants

There is no safe, openly licensed Australian bush-tucker manual that this project can ship. Do not add a scanned commercial book.

| Material | How |
|---|---|
| Richard Graves, *Australian Bushcraft*, and other commercial guides | Buy or otherwise legally obtain them. Your files only. |
| State herbarium or flora fact sheets | Your files, unless the sheet is CC BY or CC BY-SA, in which case it can be added to `fetch_au.py` with the URL and licence. |
| Gardenology and Wikipedia plants | Already in the wiki set. Not a foraging clearance. The bush-skills note tells the model not to name something as dinner. |

## Energy

| Material | Licence, as checked | How |
|---|---|---|
| YourHome renewable energy, batteries, photovoltaic systems | CC BY 4.0, Commonwealth of Australia (DCCEEW). https://www.yourhome.gov.au/copyright | `python3 library/fetch_au.py`. If the site blocks the download, print or save the HTML into Your files. |
| Geoscience Australia earthquake pages (drop, cover, hold) | CC BY 4.0, Commonwealth of Australia (Geoscience Australia). https://www.ga.gov.au/copyright checked 2026-10-26. Excludes the Coat of Arms, the logo, third-party content, and any page with its own copyright line | `python3 library/fetch_au.py`. The field note is original text and does not copy the page. |
| Energypedia and Appropedia small-hydro and solar articles | CC BY-SA | Kiwix, via `library/fetch_zims.py` |
| Pico Hydro for Village Power, Maher & Smith, 2001, picohydro.org.uk | No reproduction licence found in the chapters | `fetch_manuals.py --personal` or Your files. Not in the base library. |
| NRCan Micro-Hydropower Systems: A Buyer's Guide (2004) | Crown copyright. Read the notice inside the PDF before any sharing | `--personal` or Your files. The fetch URL may change; if it fails, take the PDF from Natural Resources Canada yourself. |
| NCAT/ATTRA Micro-Hydro Power: A Beginners Guide to Design and Installation | © NCAT. https://attra.ncat.org/publication/micro-hydro-power-a-beginners-guide-to-design-and-installation/ | `--personal` or Your files. |
| Practical Action micro-hydro technical briefs | Not confirmed as CC BY or CC BY-SA for the set. Do not assume a share licence | If the file you downloaded says CC BY or CC BY-SA on it, add it under `manuals/open`. If not, Your files. |
| Bureau of Meteorology warning pages | Commonwealth copyright. Not cleared here as CC BY. The field notes tell you to follow a warning. They do not copy the Bureau's pages | Your files, if you save a page for yourself. |
| State health fact sheets (smoke, mosquitoes, sanitation) | Not CC BY as a class. A single page can be fetched later only when that page's footer says CC BY | Your files. |
| St John first-aid sheets and Clean Energy Council battery guides | Copyright. Free to read, useful, not redistributed | Your files. |
| Generator and inverter manuals for the machine you own | The manufacturer's copyright | Your files. The field notes cover carbon monoxide, backfeed, and load priority only. |

## Numbers the field notes use

These are public service numbers, not a document we republish:

- **000** — police, fire, ambulance. **112** from a mobile with no signal. **106** textphone.
- **132 500** — SES storm and flood.
- **13 11 26** — Poisons Information Centre.
- **1800 022 222** — Healthdirect.
- **1800 679 737** — NSW RFS bush fire information only.
- **1800 226 226** — Victoria, VicEmergency information hotline. Not staffed around the clock outside major incidents.
- **1800 362 361** — South Australia, CFS Information Hotline.
- **13 3337** — Western Australia, DFES information.
- **1800 000 699** — Tasmania Fire Service Information Line.
- Queensland, the ACT and the Northern Territory: no fire-information number is stored. Do not invent one.
- **1800 278 462** — Asthma Australia. Information, not an ambulance.

## Rebuild, short version

```bash
python3 -m venv .venv && .venv/bin/pip install libzim lxml trafilatura
python3 library/fetch_au.py
python3 library/fetch_zims.py          # large; needs the Kiwix catalog
python3 library/build_library.py       # field notes plus whatever open downloads succeeded
```

The field notes alone are enough to build a small index and try the app. Wikipedia and the other ZIMs are what make the library large. They are optional in the sense that the app runs without them, and they are the right open encyclopedia layer when you have the disk.
