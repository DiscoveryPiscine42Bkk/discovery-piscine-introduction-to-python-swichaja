import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    steing_to_search = sys.argv[2]
    occurrences = re.fibdall(re.escape(keyword), string_to_seach)
    print(len(occurrences))
else:
    print("none")