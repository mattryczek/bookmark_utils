import sys, json


INDENT_LEVEL = 3
INDENT = ' ' * INDENT_LEVEL

def folder_walk(folder, level):
    count = 0

    for child in folder['children']:
        if child['typeCode'] == 1:
            count = count + 1

    print(f"{INDENT * level} 📂 {folder['title']} [{count}]")

    for child in folder['children']:
        # if child['typeCode'] == 1:
        #     print(f"{INDENT * (level + 1)} {child['title']}")

        if child['typeCode'] == 2:
            folder_walk(child, level + 1)

    return count


def main():
    filename = str(sys.argv[1])

    print(f"\n[OK] Using {filename}")

    try:
        f = open(filename, encoding='utf8')
        print("[OK] File read successful\n")
    except:
        print("[FATAL] Could not open file")
        exit()

    data = json.load(f)
    total_bookmarks = 0
    total_duplicates = 0
    folders = data['children']

    print(f"💼 {filename}:")

    for folder in folders:
        try:
            total_bookmarks = total_bookmarks + folder_walk(folder, 1)

        except:
            # If a folder has no items there is no 'children' key
            pass

    print()
    print(f"[INFO] File containts {total_bookmarks} total bookmarks")
    print()

if __name__ == "__main__":
    main()

