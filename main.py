import os

ENTRY = (
    "A traffic jam is a parking lot that forgot it was supposed to move.\n"
    "It maps the rows of stopped cars and the waiting, but it leaves out "
    "the honking, the impatience, and the fact that nobody parked there is "
    "late for anything."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
