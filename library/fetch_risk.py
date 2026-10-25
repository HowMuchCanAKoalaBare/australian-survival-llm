"""US mortality and micromort downloads are disabled in this fork.

The upstream project fetched US Social Security life tables, CDC mortality briefs,
NHTSA crash statistics and National Weather Service lightning odds. Those figures
do not describe Australian risk and are not part of the default library.

Usage: python3 library/fetch_risk.py
This script does not download anything. It remains so older instructions fail softly.
"""
import sys

print("fetch_risk.py: disabled in the Australian fork.")
print("US life tables, CDC mortality, NHTSA crash data and NWS lightning odds are not indexed.")
print("See AUSTRALIAN_SOURCES.md. Do not treat a US micromort table as an Australian risk.")
sys.exit(0)
