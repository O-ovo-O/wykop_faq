from dataclasses import dataclass

@dataclass
class TabRow:
    name: str
    link: str = ""
    lang: str = "?"
    def __post_init__(self):
        for i in self.__dict__.keys():
            setattr(self, i, getattr(self, i).strip())
    def __repr__(self):
        return f"| {self.name} | {self.link} | {self.lang} |"

with open("elektronika.md") as f:
    lines = f.readlines()

rows = []
for line in lines:
    if not line.startswith("  - "):
        continue
    line = line[4:]
    items = line.split(" - ")
    match len(items):
        case 3 | 2:
            t = TabRow(*items)
        case 1:
            t = TabRow(items[0])
    rows.append(t)

header = f"| name | link | lang |\n|:---:|:---:|:---:|\n"
footer = "\n\nJeśli chcesz dodać pozycję, dodaj ją w elektronika.md"\
         ", tabela w tym pliku jest generowana"
with open("elektronika_table_readonly.md", 'w') as f:
    f.write(header)
    for row in rows:
        f.write(repr(row))
        f.write('\n')
    f.write(footer)
