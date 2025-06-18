import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    string_to_seach = sys.argv[2]
    occurrences = re.finda11(keyword, steing_to_search)
    print(len(occurrences))
else:
    print("none")