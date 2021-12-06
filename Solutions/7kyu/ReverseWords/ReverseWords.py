# TASK:  REVERSE WORDS
# Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.

# Examples:
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
import re


def reverse_words(text: str) -> str:
    return ''.join(word[::-1] for word in re.findall(r"\w+[.,?!:;]*|\s*", text))
