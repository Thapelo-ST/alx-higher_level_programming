#!/usr/bin/python3
"""
prints the string until the encounter of . ? and :
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text:
        res = ""
        delims = [".", ":", "?"]
        prev_char = ""

        for c in text:
            if c in delims:
                if prev_char == c:
                    continue
                res += c + "\n\n"
            else:
                res += c
            prev_char = c

        print(res)
