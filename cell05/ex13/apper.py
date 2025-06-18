import sys 
import re 

args = sys.argv[1:]

if not arags:
    print("none")
else:
    for word in args:
        print("none")
else:
  for word in args:
    if not re.search(r'ism$',word):
       print(f"{word}ism")