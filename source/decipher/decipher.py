import re
import sys

MAX_TEXT_LENGTH = 100000


class ValidationError(Exception):
    pass


def validate_input(txt):
    if len(txt) > MAX_TEXT_LENGTH or re.findall(r"[^a-z]+", txt.lower()):
        raise ValidationError(
            f"Text have to be shorter than {MAX_TEXT_LENGTH} and include only [a-z]"
        )


def is_identical_letter(txt, index):
    return txt[index] == txt[index - 1]


def decipher(txt):
    validate_input(txt)
    res = []
    i = 1
    while i < len(txt):
        if not is_identical_letter(txt, i):
            res.append(txt[i - 1])
            if i == len(txt) - 1:
                res.append(txt[i])
            i = i + 1
        else:
            i = i + 2
    return ''.join(res)


input_txt = open(sys.argv[1])
text = input_txt.read()
input_txt.close()

print(decipher(text))
