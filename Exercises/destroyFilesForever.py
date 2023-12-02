from pathlib import Path

root_dir = Path('files_3')

for path in root_dir.glob("*.txt"):
    with open(path, 'wb') as file:
        file.write(b'')
    path.unlink()
