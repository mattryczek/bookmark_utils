# Bookmark Utils

A small tool written in Python that de-duplicates bookmarks. Currently works with Firefox JSON bookmark export files.

## To-Do
+ ~~Nested folder support~~
+ Automatic file location search (default Firefox path)
+ Backup original list function
+ Rust impl?

## Usage

```
python3 clean.py <bookmark_file>.json
```

## Chrome Bookmarks
Chrome only exports bookmarks in HTML format. There is a roundabout way to convert to JSON...

1. Export Chrome bookmark HTML file.
2. Using Firefox, import bookmarks (optionally into a separate profile).
3. Export bookmarks from Firefox, choosing JSON format.

The de-duplicated list can be added back into Firefox, exported as HTML, and ingested by Chrome.