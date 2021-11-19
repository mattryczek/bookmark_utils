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
        return {each['uri'] : each for each in folder['children']}.values()
    except:
        pass

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
            unique_bookmarks = deduplicate(folder)

            folder['children'] = []
            for item in unique_bookmarks:
                folder['children'].append(item)

        except:
            # If a folder has no items there is no 'children' key
            pass

    TREE.reverse()
    for line in TREE:
        print(line)

    print(f"\n[INFO] Total bookmarks in file: {total_bookmarks}")
    print(f"[INFO] Duplicate bookmarks: {total_bookmarks - len(TEST)} ({((total_bookmarks - len(TEST))/total_bookmarks * 100):.2f}%)")
    print(f"\n[OK] Rebuilt bookmark file with {len(unique_bookmarks)} unique bookmarks")

    try:
        with open(f"clean_{filename}", 'w') as outfile:
            json.dump(data, outfile)
            print(f"[OK] New bookmark file saved")
            print()
    except:
        print(f"[FATAL] Could not write to outfile")
        exit()


if __name__ == "__main__":
    main()

