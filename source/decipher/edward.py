import re
import sys
import unittest

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
            f"File must have '.txt' extension"
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
    input_txt = open(file)
    text = input_txt.read()
    input_txt.close()
    return validate_input(text)


if __name__ == "__main__":
    validate_extension(FILE)
    decipher(get_cipher(FILE))


    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(decipher(get_cipher(FILE)), "edward")


    unittest.main(argv=['first-arg-is-ignored'], exit=False)
