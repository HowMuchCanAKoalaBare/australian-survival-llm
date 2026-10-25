"""Download manuals that are not in a Kiwix ZIM.

Usage:
  python3 library/fetch_manuals.py              # open manuals only (redistributable)
  python3 library/fetch_manuals.py --personal   # also the user-requested PDFs whose licence
                                                 # does not clearly allow redistribution
  python3 library/fetch_manuals.py --nc         # IFRC and WHO (non-commercial)

Files land in library.noindex/raw/manuals/<group>/ with a manifest.json.
Nothing in the "personal" group is part of a --public library build.
This fork does not download Ready.gov, FEMA, CDC, US military survival manuals,
Nuclear War Survival Skills, the US Emergency Response Guidebook, or the USDA canning guide.
See AUSTRALIAN_SOURCES.md before you share a library that used --personal.
"""
import hashlib
import json
import os
import subprocess
import sys

# group, title, url, licence
OPEN = []  # add a manual here only after its licence allows redistribution (CC BY, CC BY-SA, public domain, OGL)

# Requested by the Australian fork, but not cleared for the base library.
# --personal downloads them for the builder's own index. Do not publish the resulting library.
PERSONAL = [
    ("personal", "Pico Hydro for Village Power, chapters 1–6 (Maher & Smith, 2001)",
     "https://www.picohydro.org.uk/docs/impman_(ch1-6).pdf",
     "DfID-funded manual. No reproduction licence is stated in the file. Personal study only until the authors' terms are confirmed."),
    ("personal", "Pico Hydro for Village Power, chapter 9 (generators and load control)",
     "https://www.picohydro.org.uk/docs/impman_(ch9).pdf",
     "Same work as the Maher & Smith manual. Personal study only."),
    ("personal", "NCAT/ATTRA Micro-Hydro Power: A Beginners Guide to Design and Installation",
     "https://www.ncat.org/wp-content/uploads/2025/12/microhydrodesign.pdf",
     "© NCAT. Free to read on the ATTRA site. Not cleared for redistribution in this library."),
    ("personal", "Natural Resources Canada: Micro-Hydropower Systems, A Buyer's Guide (2004)",
     "https://natural-resources.canada.ca/sites/www.nrcan.gc.ca/files/canmetenergy/files/pubs/Buyers%20Guide%20to%20Micro%20Hydropower%20Systems.pdf",
     "Canadian Crown copyright. Confirm the reproduction notice inside the PDF before sharing a library that contains it."),
]

NC = [
    ("nc", "IFRC International First Aid, Resuscitation and Education Guidelines 2020",
     "https://www.ifrc.org/sites/default/files/2022-02/EN_GFARC_GUIDELINES_2020.pdf",
     "© IFRC. Copying allowed for non-commercial use with acknowledgement. Not Australian Resuscitation Council guidance."),
    ("nc", "WHO-ICRC Basic Emergency Care (2018)",
     "https://iris.who.int/server/api/core/bitstreams/63432b9f-8808-44c5-9692-cea717c0cbda/content",
     "CC BY-NC-SA 3.0 IGO. WHO does not endorse this app."),
    ("nc", "WHO: Managing Complications in Pregnancy and Childbirth (2017)",
     "https://iris.who.int/server/api/core/bitstreams/3bda1306-da5d-487d-b2ad-aff995112a7a/content",
     "CC BY-NC-SA 3.0 IGO. WHO does not endorse this app."),
    ("nc", "WHO: Guidelines for Drinking-water Quality (4th ed., 2022)",
     "https://iris.who.int/server/api/core/bitstreams/69c17edd-ee26-425b-9d34-33799377e886/content",
     "CC BY-NC-SA 3.0 IGO. The Australian reference is the NHMRC Drinking Water Guidelines, which this library does not redistribute."),
]

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 15_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "library.noindex", "raw", "manuals")


def fetch(group, title, url, licence):
    folder = os.path.join(ROOT, group)
    os.makedirs(folder, exist_ok=True)
    dest = os.path.join(folder, hashlib.sha256(url.encode()).hexdigest()[:12] + ".pdf")
    manifest_path = os.path.join(folder, "manifest.json")
    manifest = json.load(open(manifest_path)) if os.path.exists(manifest_path) else []
    if any(item["url"] == url for item in manifest) and os.path.exists(dest) and open(dest, "rb").read(4) == b"%PDF":
        print("skip    " + title, flush=True)
        return
    r = subprocess.run(["curl", "-L", "--fail", "-sS", "-A", UA, "--retry", "3", "--http1.1", "-o", dest, url])
    ok = r.returncode == 0 and os.path.exists(dest) and open(dest, "rb").read(4) == b"%PDF"
    print(("ok      " if ok else "FAILED  ") + title, flush=True)
    if not ok:
        if os.path.exists(dest):
            os.remove(dest)
        return
    manifest = [item for item in manifest if item["url"] != url]
    manifest.append({"file": os.path.basename(dest), "title": title, "url": url, "license": licence})
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=1)


def main():
    personal = "--personal" in sys.argv
    nc = "--nc" in sys.argv
    jobs = list(OPEN)
    if nc:
        jobs += NC
    if personal:
        jobs += PERSONAL
    if not jobs:
        print("No redistributable PDF manuals are on the default fetch list.")
        print("Australian government PDFs that are free to read but not free to republish")
        print("(RediPlan, ANZCOR, AIDR handbooks, NHMRC, NSW RFS, NSW SES) are documented")
        print("in AUSTRALIAN_SOURCES.md. Save those yourself into the Your files folder.")
        print("Pass --personal to download pico-hydro and related manuals for your own index.")
        print("Pass --nc to download IFRC and WHO guides (non-commercial).")
        return
    for group, title, url, licence in jobs:
        fetch(group, title, url, licence)


if __name__ == "__main__":
    main()
