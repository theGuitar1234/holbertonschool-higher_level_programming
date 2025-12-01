#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1 as calc
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> operator <b>")
        sys.exit(1)
    else:
        a, b, c = int(sys.argv[1]), int(sys.argv[3]), sys.argv[2]
        if c == "+":
            print("{} + {} = {}".format(a, b, calc.add(a, b)))
        elif c == "-":
            print("{} - {} = {}".format(a, b, calc.sub(a, b)))
        elif c == "*":
            print("{} * {} = {}".format(a, b, calc.mul(a, b)))
        elif c == "/":
            print("{} / {} = {}".format(a, b, calc.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        sys.exit(0)
