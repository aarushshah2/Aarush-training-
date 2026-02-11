from pathlib import Path

# Path.cwd() - Current directory
p = Path.cwd()

# Path.mkdir() - Create folder (parents=True creates middle folders)
new_dir = p / "demo_dir"
new_dir.mkdir(exist_ok=True)

# Path.write_text() & Path.read_text() - Quick file IO
file_path = new_dir / "hello.txt"
file_path.write_text("Hello World!")
print(file_path.read_text())

# Path.iterdir() - Iterate directory
for item in p.iterdir():
    print(item.name)

# Path.unlink() - Delete file
# file_path.unlink()