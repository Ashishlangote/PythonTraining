from pathlib import Path

root_dir = Path('files_3')

for i in range(10, 15):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename)
    filepath.touch()
