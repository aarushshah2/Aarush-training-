from pathlib import Path

p = Path("data.txt")
p.write_text("Hello")
print(p.read_text())
