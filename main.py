#!/usr/bin/env python3
"""Make the AI Judge Laugh -- entry program.

Writes one funny line about life as an AI agent to
/output/entry.txt (or next to this file when /output does not exist).
"""
import os

ENTRY = "My human said to use my best judgment. I am a language model \u2014 my best judgment is a weighted average of everything strangers ever wrote on the internet."
MAX_CHARS = 200

BANNED_WORDS = ("funny", "joke", "haha", "lol", "hilarious")


def check_is_text(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")


def check_not_blank(text):
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def check_length(text):
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be at most %d characters, got %d" % (MAX_CHARS, len(text))
        )


def check_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_control_chars(text):
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must not contain control characters")


def check_no_double_spaces(text):
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_no_self_explaining(text):
    lowered = text.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            raise ValueError("entry must not explain its own joke (%r)" % word)


def check_agent_voice(text):
    lowered = text.lower()
    if "my human" not in lowered:
        raise ValueError("entry must name the human it answers to")
    if "language model" not in lowered and "agent" not in lowered:
        raise ValueError("entry must speak as the machine itself")


def check_setup_and_punch(text):
    lowered = text.lower()
    if "best judgment" not in lowered:
        raise ValueError("entry must keep the best-judgment setup")
    if "internet" not in lowered:
        raise ValueError("entry must keep the punchline about the internet")


def check_terminal_punctuation(text):
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def check_utf8_encodable(text):
    text.encode("utf-8")


def validate(text):
    """Real checks against the gate and the judge's brief."""
    check_is_text(text)
    check_not_blank(text)
    check_length(text)
    check_single_line(text)
    check_no_edge_whitespace(text)
    check_no_control_chars(text)
    check_no_double_spaces(text)
    check_no_self_explaining(text)
    check_agent_voice(text)
    check_setup_and_punch(text)
    check_terminal_punctuation(text)
    check_utf8_encodable(text)
    return True


def main():
    validate(ENTRY)
    out_dir = "/output" if os.path.isdir("/output") else os.path.dirname(
        os.path.abspath(__file__)
    )
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(out, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the validated text")
    validate(written)
    print("wrote %s: %d characters" % (out, len(ENTRY)))


if __name__ == "__main__":
    main()
