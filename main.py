"""One Line, One Chill — writes a single-sentence horror line to entry.txt."""

import os

# One sentence, one breath: the dead don't call — and the thing upstairs is learning to be you.
LINE = "My dead grandmother's voicemail said the man in our attic has finally learned to sound like me."


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
