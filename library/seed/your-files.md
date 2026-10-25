# Adding your own files

**Licence:** CC BY 4.0, Australian Survival LLM field notes.

## What the base library refuses to include

The base library only holds material that is public domain, government free-to-use, or openly licensed (CC BY, CC BY-SA, or the UK Open Government Licence for the medicines dump). It does not contain:

- Australian Red Cross RediPlan (copyright, free to read, not cleared here for redistribution)
- ANZCOR / Australian Resuscitation Council guidelines (download them yourself)
- AIDR Disaster Resilience Handbooks (CC BY-NC, so not in the public pack)
- NHMRC Australian Drinking Water Guidelines (personal or internal copying only, as stated by NHMRC)
- NSW RFS and NSW SES fact sheets (save the PDFs from the agencies)
- Commercial books: SAS Survival Handbook, Richard Graves' Australian Bushcraft, bush-tucker field guides, manufacturer manuals you bought

## How to add them

In the local app, Your files is at the top of the window. Drop PDFs, Word documents, EPUB books, web pages saved as HTML, or text files. They are indexed on that computer only, in the Australian Survival LLM Files folder in your home folder. You can also put files straight into that folder. Scans that are only photographs of pages are not readable yet. Use a PDF with real text, or run OCR yourself first.

Rebuild is not required for Your files. The app picks them up. Rebuilding the shared library (`library/build_library.py`) is for sources you add to the fetch scripts, not for a PDF on the kitchen table.

## Making a personal source part of a rebuilt library

If you have the right to hold a PDF and you want it in the big index rather than only in Your files, that is the `--personal` path described in AUSTRALIAN_SOURCES.md. Do not publish that index. Other people's copyright does not become free because it is sitting next to Wikipedia.

## After you add a file

Ask the question again. Your files outrank a general article when both talk about your generator, your rainwater pump, or your medicine list. Read the passage the app highlights. The model is still a model.
