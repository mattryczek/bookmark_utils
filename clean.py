import sys, json

filename = str(sys.argv[1])

print(f"\n[OK] Filename: {filename}")

try:
    f = open(filename, encoding='utf8')
    print("[OK] File read successful")
except:
    print("Could not open file")
    exit()

data = json.load(f)

folders = data['children']

print("[INFO] Found folders:\n")
for folder in folders:
    try:
        count = len(folder['children'])
    except:
        # If a folder has no items there is no 'children' key
        count = 0

    print(f"{folder['title']} [{count}]")


# print(json.dumps(folders))