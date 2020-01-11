# Autori
import sys

inputstd = sys.stdin.read()
words = inputstd.split('-')
output = ''.join(word[0] for word in words)
print(output)