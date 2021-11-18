import sys, json

filename = str(sys.argv[1])

print(f"\n[OK] Using {filename}")

try:
    f = open(filename, encoding='utf8')
    print("[OK] File read successful")
except:
    print("[FATAL] Could not open file")
    exit()

data = json.load(f)

folders = data['children']
clean = set()

print("[INFO] Found folders:\n")
print(f"{filename}:")

for folder in folders:
    try:
        count = len(folder['children'])
        for bookmark in folder['children']:
            clean.add(bookmark['uri'])

        count = str(count) + f", {count - len(clean)} duplicates"

    except:
        # If a folder has no items there is no 'children' key
        count = 0

    print(f"  📂 {folder['title']} [{count}]")
    clean = set()

print()
