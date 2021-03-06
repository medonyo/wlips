import re
import sys

with open("./wlip-0003/preliminary-word-lists/english_us") as f:
    lines = f.readlines()

    words = []
    for line in lines:
        word_match = re.match(r'(^\w+)\n', line)

        if word_match is None:
            continue

        word = word_match.group(1)
        if word in words:
            print("error: first duplicated word on english_us: '{}'".format(word))
            sys.exit(1)

        words.append(word)

    print("success: english_us has no duplicated words")
    sys.exit(0)
