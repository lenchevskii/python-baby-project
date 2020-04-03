import re
import sys

extension_types = {
    'json': '.json',
    'csv': '.csv',
    'xml': '.xml',
    'bin': '.bin'
}

INPUT_FILENAME = sys.argv[1]
OUTPUT_FILENAME = sys.argv[2]
PATTERN = r"([a-zA-Z0-9\s_\\.\-\(\):])+(.json|.csv|.xml|.bin)$"


def get_extension_type(filename, pattern):
    return re.search(pattern, filename).group(2)


# print(sys.argv[1:])
#
# import xmltodict
# import pprint
# import json
#
# my_xml = """ <audience> <id what="attribute">123</id> <name>Shubham</name> </audience> """
#
# # print(json.dumps(my_xml, indent=4, sort_keys=True))
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(json.dumps(xmltodict.parse(my_xml)))
import xmltodict, json

with open('sample.xml') as inFh:
    with open('sample.json', 'w') as outFh:
        json.dump(xmltodict.parse(inFh.read()), outFh)
