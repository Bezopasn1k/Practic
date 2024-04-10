import sys
text = sys.stdin.read()
def wordcounter(text):
    words = text.split()
    uniq = set(words)
    return len(uniq)
print(wordcounter(text))