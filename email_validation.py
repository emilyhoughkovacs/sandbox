import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test:
        continue
    if re.match('([\w]+[.]?[a-zA-z0-9]+)+@([a-zA-z1-9]+[.]?[-a-zA-z1-9]+)+[.][a-zA-Z]+', test):
        print("true")
    else:
        print("false")

test_cases.close()