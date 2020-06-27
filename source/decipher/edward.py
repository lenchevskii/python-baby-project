import re
import sys
from functools import reduce
from pathlib import PurePosixPath

MAX_TEXT_LENGTH = 100000

FILE = sys.argv[1]


class ValidationError(Exception):
    pass


def validate_input(txt):
    if len(txt) > MAX_TEXT_LENGTH or re.findall(r"[^a-z]+", txt):
        raise ValidationError(
            f"Text should be shorter than {MAX_TEXT_LENGTH} and include only [a-z]"
        )
    return txt


def validate_extension(file):
    if not file.endswith('.txt'):
        raise ValidationError(
            f"File must have '.txt' extension, but got '{PurePosixPath(file).suffix}'"
        )
    return file


def is_identical_letter(txt, index):
    return txt[index] == txt[index - 1]


def is_last_letter(txt, index):
    return index == len(txt) - 1


def decipher(txt):
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


def get_cipher(file):
    with open(file) as text:
        return validate_input(text.read())


def compose(*fns):
    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)


if __name__ == "__main__":
    message = compose(decipher, get_cipher, validate_extension)
    print(message(FILE), end='')
