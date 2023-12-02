from pathlib import Path

root_dir = Path('files_2')
search_term = '02'

for path in root_dir.rglob("*"):
    if path.is_file():
        if search_term in path.stem:
            print(path.absolute())
