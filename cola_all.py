#!/usr/bin/env python3
import pathlib
import json

def main():
    file = pathlib.Path("~/.config/git-cola/settings").expanduser()
    data = json.loads(file.read_text())

    bookmarks = []

    for parent_folder in pathlib.Path("~").expanduser().glob("src*"):
        for folder in parent_folder.iterdir():
            if not (folder / ".git").exists():
                continue
            print(f"[{parent_folder.name}] {folder.name} -> {folder}")
            bookmarks.append({
                'path': f"{folder}",
                'name': f"[{parent_folder.name}] {folder.name}"
            })
    data["bookmarks"] = bookmarks
    file.write_text(json.dumps(data))

if __name__ == "__main__":
    main()
