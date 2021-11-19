# Bookmark Utils

A small tool written in Python that de-duplicates bookmarks. Currently works with Firefox JSON bookmark export files.

## Warning

As of this commit the tool works only on flat bookmark file structures (i.e. all your bookmarks are in the built in "Other Bookmarks" or "Mobile Bookmarks" folder). This message will self destruct once the tool learns how to traverse and prune nested directories.

## Usage

```
python3 clean.py <bookmark_file>.json
```

## To-Do
+ Support for nested folders (preserve hierarchy)
+ ~~Tree View~~
  + Done!
+ Automatic file location search (default Firefox path)
+ ~~Backup original list function~~
  + Script preserves original file instead
+ ~~Rust impl?~~
  + Nah...

## Chrome Bookmarks
Chrome only exports bookmarks in HTML format. There is a workaround however to convert to JSON...

1. Export Chrome bookmark HTML file.
2. Using Firefox, import bookmarks (optionally into a separate profile).
3. Export bookmarks from Firefox, choosing JSON format.

The de-duplicated list can be added back into Firefox, exported as HTML, and ingested by Chrome.