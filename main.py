"""One-Line Office Joke Laugh-Off — one office joke, one line.

Entry: "This meeting has lasted so long my laptop offered to auto-save
my will."
Gate: /output/entry.txt, UTF-8, 1-200 chars, not whitespace-only, one line.
Judge: pairwise comparison by an AI judge. The humour must come from a
painfully relatable office truth — a meeting so long it outlasts a will —
told deadpan, with the laptop as the only honest witness in the room.
"""
import os

ENTRY = "This meeting has lasted so long my laptop offered to auto-save my will."


def main():
    # Gate self-check: 1-200 chars, single line, not blank.
    assert 1 <= len(ENTRY) <= 200, f"length {len(ENTRY)} outside 1-200"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
