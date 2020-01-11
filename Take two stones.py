# Take two stoness
import sys

stones = int(sys.stdin.read())
if stones % 2 == 1:
    print('Alice')
else:
    print('Bob')