import sys, json


INDENT_LEVEL = 3
INDENT = ' ' * INDENT_LEVEL
TEST = set()
TREE = []

def folder_walk(folder, level):
    count = 0

    for child in folder['children']:
        if child['typeCode'] == 1:
            count = count + 1
            TEST.add(child['uri'])
        else:
            count = count + folder_walk(child, level + 1)

    TREE.append(f"[{count}]{INDENT * level}📂 {folder['title']}")

    return count


def deduplicate(folder):
    try:
        unique_uris = {each['uri'] : each for each in folder['children']}.values()
    except:
        pass

    # for item in unique_uris:
    #     print(json.dumps(item, indent=2))


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
            deduplicate(folder)

        except:
            # If a folder has no items there is no 'children' key
            pass

    
    TREE.reverse()
    for line in TREE:
        print(line)

    print()
    print(f"[INFO] Total bookmarks in file: {total_bookmarks}")
    print(f"[INFO] Duplicate bookmarks: {total_bookmarks - len(TEST)} ({((total_bookmarks - len(TEST))/total_bookmarks * 100):.2f}%)")
    print()


if __name__ == "__main__":
    main()

