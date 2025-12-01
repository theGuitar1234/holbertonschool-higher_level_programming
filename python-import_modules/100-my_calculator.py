#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1 as calc
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> operator <b>")
        sys.exit(1)
    else:
        a, b = int(sys.argv[1]), int(sys.argv[3])
        match sys.argv[2]:
            case "+":
                print("{} + {} = {}".format(a, b, calc.add(a, b)))
            case "-":
                print("{} - {} = {}".format(a, b, calc.add(a, b)))
            case "*":
                print("{} * {} = {}".format(a, b, calc.add(a, b)))
            case "/":
                print("{} / {} = {}".format(a, b, calc.add(a, b)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
        sys.exit(0)

