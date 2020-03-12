import re
import sys


def decipher(txt):
    if len(txt) < 100000 and re.findall(r"[\W|\d|_|A-Z]", txt) == []:
        res = ''
        i = 1
        while i < len(txt):
            if txt[i] != txt[i - 1]:
                res += ''.join(txt[i - 1])
                if i == len(txt) - 1:
                    res += ''.join(txt[i])
                i = i + 1
            else:
                i = i + 2
        return res
    else:
        return 'This is a trapppp!'


input_txt = open(sys.argv[1])
text = input_txt.read()
input_txt.close()

print('deciphered message:', decipher(text))
