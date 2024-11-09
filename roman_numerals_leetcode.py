def roman_to_int(s: str) -> int:
    # roman_numerals = {
    #     "I": 1,
    #     "V": 5,
    #     "X": 10,
    #     "L": 50,
    #     "C": 100,
    #     "D": 500,
    #     "M": 1000,
    #     "IV": 4,
    #     "IX": 9,
    #     "XL": 40,
    #     "XC": 90,
    #     "CD": 400,
    #     "CM": 900
    # }
    # new_num = 0
    #
    # while len(s) > 1:
    #     if roman_numerals.get(s[0]+s[1]) is not None:
    #         new_num += roman_numerals[s[0] + s[1]]
    #         s = s[2:]
    #     else:
    #         new_num += roman_numerals[s[0]]
    #         s = s[1:]
    # if len(s) != 0:
    #     new_num += roman_numerals[s[0]]
    #
    # return new_num

    # roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    # result = 0
    # for i, c in enumerate(s):
    #     if (i+1) == len(s) or roman_numerals[c] >= roman_numerals[s[i+1]]:
    #         result += roman_numerals[c]
    #     else:
    #         result -= roman_numerals[c]
    # return result

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    n = len(s)
    result = roman[s[n - 1]]
    print(result)

    for i in range(n - 2, -1, -1):
        if roman[s[i]] < roman[s[i + 1]]:
            result = result - roman[s[i]]
            print(result)
        else:
            result = result + roman[s[i]]
            print(result)

    return result


roman_number = input("Type in a roman number and this program will convert it into arabic numbers: ")

print(roman_to_int(roman_number))
