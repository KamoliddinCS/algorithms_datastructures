import roman

def roman_to_int(s: str) -> int:
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    new_num = 0

    while len(s) > 1:
        if roman_numerals.get(s[0]+s[1]) is not None:
            new_num += roman_numerals[s[0] + s[1]]
            s = s[2:]
        else:
            new_num += roman_numerals[s[0]]
            s = s[1:]
    if len(s) != 0:
        new_num += roman_numerals[s[0]]

    return new_num


roman_number = input("Type in a roman number and this program will convert it into arabic numbers: ")

print(roman_to_int(roman_number))