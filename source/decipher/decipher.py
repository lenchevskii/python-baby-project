import re
import sys

# partial_res = reduce(lambda acc, a: acc + a if acc[-1] != a else acc, test_str)
if len(sys.argv) > 1:
    input_txt = open(sys.argv[1])
    text = input_txt.read()
    input_txt.close()

    def decipher(txt):
        if len(txt) < 100000 and re.findall(r"[\W|\d|_|A-Z]", txt) == []:
            res = ''
            i = 1
            while i < len(txt):
                if txt[i] != txt[i - 1]:
                    res += res.join(txt[i - 1])
                    i = i + 1
                else:
                    i = i + 2
            return res
        else:
            return 'This is a trapppp!'

    print('deciphered message:', decipher(text))
else:
    print('Give me a cipher, pleas.')
