#!./venv/bin/python3
import sys
import c5kyu.some_egyptian_fractions as test

if len(sys.argv) > 1:
    print(test.decompose(sys.argv[1]))
else:
    n = 100
    for i in range(n):
        print(f"\n\n{i}/{n}")
        print(test.decompose(f"{i}/{n}"))