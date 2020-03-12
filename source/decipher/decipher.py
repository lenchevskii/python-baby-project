import re
import sys


def is_message(txt):
    return len(txt) < 100000 and re.findall(r"[^a-z]+", txt) == []


def is_identical_letters(txt, index):
    return txt[index] == txt[index - 1]


def decipher(txt):
    if is_message(txt):
        res = []
        i = 1
        while i < len(txt):
            if not is_identical_letters(txt, i):
                res.append(txt[i - 1])
                if i == len(txt) - 1:
                    res.append(txt[i])
                i = i + 1
            else:
                i = i + 2
        return ''.join(res)
    return 'This is a trapppp!'


input_txt = open(sys.argv[1])
text = input_txt.read()
input_txt.close()

print('deciphered message:', decipher(text))
