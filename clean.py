import sys, json


INDENT_LEVEL = 3
INDENT = ' ' * INDENT_LEVEL
TEST = set()

def folder_walk(folder, level):
    count = 0

    for child in folder['children']:
        if child['typeCode'] == 1:
            count = count + 1

    print(f"[{count}]{INDENT * level}📂 {folder['title']}")

    for child in folder['children']:
        if child['typeCode'] == 1:
            TEST.add(child['uri'])
        #     print(f"{INDENT * (level + 1)} {child['title']}")

        if child['typeCode'] == 2:
            count = count + folder_walk(child, level + 1)

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
    folders = data['children']

    print(f"💼 {filename}:")

    for folder in folders:
        try:
            total_bookmarks = total_bookmarks + folder_walk(folder, 1)

        except:
            # If a folder has no items there is no 'children' key
            pass

    print()
    print(f"[INFO] Total bookmarks in file: {total_bookmarks}")
    print(f"[INFO] Duplicate bookmarks: {total_bookmarks - len(TEST)} ({((total_bookmarks - len(TEST))/total_bookmarks * 100):.2f}%)")
    print()


if __name__ == "__main__":
    main()

