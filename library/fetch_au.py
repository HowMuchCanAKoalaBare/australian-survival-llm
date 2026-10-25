"""Download Australian pages whose site licence is CC BY 4.0.

Usage: python3 library/fetch_au.py
Saves HTML into library.noindex/raw/au-open/ plus manifest.json for build_library.py.

Pages that come back as an empty JavaScript shell are skipped. If a download fails,
save the page yourself (Print to PDF, or the site's own PDF) and put it in Your files.
Checked 2026-10-26:
- YourHome (yourhome.gov.au) is CC BY 4.0, Commonwealth of Australia (DCCEEW).
- FSANZ website material is CC BY 4.0 Australia, except the logo and third-party material.
"""
import json
import os
import re
import subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 15_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "library.noindex", "raw", "au-open")

# (file, title, url, licence)
PAGES = [
    ("yourhome-renewable.html", "YourHome: Renewable energy",
     "https://www.yourhome.gov.au/energy/renewable-energy",
     "CC BY 4.0, Commonwealth of Australia (DCCEEW). Your Home, yourhome.gov.au. Not an endorsement."),
    ("yourhome-batteries.html", "YourHome: Batteries",
     "https://www.yourhome.gov.au/energy/batteries",
     "CC BY 4.0, Commonwealth of Australia (DCCEEW). Your Home, yourhome.gov.au. Not an endorsement."),
    ("yourhome-pv.html", "YourHome: Photovoltaic systems",
     "https://www.yourhome.gov.au/energy/photovoltaic-systems",
     "CC BY 4.0, Commonwealth of Australia (DCCEEW). Your Home, yourhome.gov.au. Not an endorsement."),
    ("fsanz-foodborne.html", "FSANZ: Prevention of foodborne illness",
     "https://www.foodstandards.gov.au/consumer/prevention-of-foodborne-illness",
     "CC BY 4.0 Australia, Food Standards Australia New Zealand. Not an endorsement."),
    ("fsanz-consumer.html", "FSANZ: Consumer information",
     "https://www.foodstandards.gov.au/consumer",
     "CC BY 4.0 Australia, Food Standards Australia New Zealand. Not an endorsement."),
]


def visible_text(html):
    text = re.sub(r"(?is)<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", html)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def main():
    os.makedirs(ROOT, exist_ok=True)
    manifest = []
    for name, title, url, licence in PAGES:
        dest = os.path.join(ROOT, name)
        r = subprocess.run(
            ["curl", "-L", "--fail", "-sS", "-A", UA, "--retry", "2", "--http1.1", "-o", dest, url],
            capture_output=True)
        if r.returncode != 0 or not os.path.exists(dest):
            print("FAILED  " + title, flush=True)
            if os.path.exists(dest):
                os.remove(dest)
            continue
        text = visible_text(open(dest, encoding="utf-8", errors="replace").read())
        if len(text) < 2500 or "you need to enable JavaScript" in text:
            print("SKIP    " + title + " (page had no article text; save it yourself)", flush=True)
            os.remove(dest)
            continue
        manifest.append({"file": name, "title": title, "url": url, "license": licence, "kind": "web"})
        print("ok      " + title, flush=True)
    with open(os.path.join(ROOT, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=1)
    print(f"{len(manifest)} pages")


if __name__ == "__main__":
    main()
