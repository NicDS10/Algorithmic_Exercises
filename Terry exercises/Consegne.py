#
#

import sys

sys.stdin = open('Terry_tests.py', 'r')

def main():
    data_momentanea = map(int, sys.stdin.read().split())
    n_casi = next(data_momentanea)
    data = list(data_momentanea)
    print(data)

if __name__ == '__main__':
    main()
