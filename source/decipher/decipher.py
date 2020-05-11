import re
import sys

MAX_TEXT_LENGTH = 100000


class ValidationError(Exception):
    pass


def validate_input(txt):
    if len(txt) > MAX_TEXT_LENGTH or re.findall(r"[^a-z]+", txt):
        raise ValidationError(
            f"Text should be shorter than {MAX_TEXT_LENGTH} and include only [a-z]"
        )


def validate_extention():
    if not sys.argv[1].endswith('.txt'):
        raise ValidationError(
            f"File must have '.txt' extention"
    )

def is_identical_letter(txt, index):
    return txt[index] == txt[index - 1]


def is_last_letter(txt, index):
    return index == len(txt) - 1


def decipher(txt):
    validate_input(txt)
    res = []
    i = 1
    while i < len(txt):
        if not is_identical_letter(txt, i):
            res.append(txt[i - 1])
            if is_last_letter(txt, i):
                res.append(txt[i])
            i = i + 1
        else:
            i = i + 1
            if is_last_letter(txt, i):
                res.append(txt[i])
            i = i + 1
    return ''.join(res)


if __name__ == "__main__":
    validate_extention()

    input_txt = open(sys.argv[1])
    text = input_txt.read()
    input_txt.close()

    print(decipher(text))
