#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    ops = {
        "+": add(a, b),
        "-": sub(a, b),
        "*": mul(a, b),
        "/": div(a, b)}
    if op in ops.keys():
        print("{:d} {} {:d} = {:d}".format(a, op, b, ops[op]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
