# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """
    Perform basic arithmetic operations based on command-line arguments.

    The script expects four command-line arguments:
    1. The first number (float or int).
    2. The operator (one of '+', '-', '*', '/', '%').
    3. The second number (float or int).

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If the operator is not one of '+', '-', '*', '/', '%'.
        ZeroDivisionError: If division by zero is attempted.

    Example:
        $ python script.py 5 + 3
        8.0
    """
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
