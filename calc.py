# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys

def main():
    if sys.argv[2] == "+":
        return float(sys.argv[1]) + float(sys.argv[3])
    if sys.argv[2] == "-":
        return float(sys.argv[1]) - float(sys.argv[3])
    if sys.argv[2] == "*":
        return float(sys.argv[1]) * float(sys.argv[3])
    if sys.argv[2] == "/":
        return float(sys.argv[1]) / float(sys.argv[3])
    if sys.argv[2] == "%":
        return float(sys.argv[1]) % float(sys.argv[3])


if __name__ == "__main__":
    print(main())
