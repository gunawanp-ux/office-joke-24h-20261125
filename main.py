"""One-line office joke for make.fun's "One-Line Office Joke: 24-Hour Sprint".

Construction of the joke in LINE:
- Setup: the colleague who opens every interruption with "quick question",
  the most dreaded two words in open-plan office life.
- Misdirection: the reader expects the payoff to be that the question is
  never quick. That lands first, as the middle clause.
- Payoff, saved for the last three words: several of these "questions"
  were not even questions at all -- they were assignments wearing a
  question's name badge. The laugh is the recognition that "quick
  question" is office code for "I am about to hand you my work." The
  em dash before "three years in" marks the beat where the setup turns.
- Economy: one sentence, every clause either loads the setup or fires a
  payoff; nothing can be cut without losing the time span ("three
  years in") or the second twist.

The program writes the single line to /output/entry.txt, as the
competition's grader expects, and also prints it to stdout.
"""

import os

LINE = "My coworker opens every interruption with 'quick question' — three years in, not one has been quick, and several weren't even questions."

def main() -> None:
    assert 1 <= len(LINE) <= 200, "joke must be between 1 and 200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "joke must be a single line"
    assert "  " not in LINE, "joke must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
