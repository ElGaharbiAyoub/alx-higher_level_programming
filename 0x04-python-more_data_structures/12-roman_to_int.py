def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rst = 0
    prevValue = 0
    romanDict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    for number in reversed(roman_string):
        value = romanDict.get(number, 0)

        if value >= prevValue:
            rst += value
        else:
            rst -= value

        prevValue = value

    return rst
