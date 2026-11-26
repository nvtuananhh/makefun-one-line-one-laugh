# One Line, One Laugh — final version
# Writes a single funny line to entry.txt.
# One twist, packed into the final words: the outage lasts 12 minutes,
# and the punchline is that the family are strangers to each other.
import os

ENTRY = "The Wi-Fi went down for 12 minutes and my family discovered we live with strangers."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
