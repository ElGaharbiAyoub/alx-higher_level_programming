def roman_to_int(roman_string):
    rst = 0
    if (roman_string and isinstance(roman_string, str)):
        romanDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prevValue = 0

        for number in reversed(roman_string):
            value = romanDict.get(number, 0)

            if value >= prevValue:
                rst += value
            else:
                rst -= value

            prevValue = value

    return rst
