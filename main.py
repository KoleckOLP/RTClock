import time
from datetime import datetime
# My own code
from kolreq.kolreq import clear


def romanNum(roman: str, numOfDigit: int, digit: str):
    if numOfDigit == 10:
        digit = digit[-2]
        romanSet = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    elif numOfDigit == 100:
        digit = digit[-3]
        romanSet = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    elif numOfDigit == 1000:
        digit = digit[-4]
        romanSet = ["M", "MM", "MMM"]
    else:
        digit = digit[-1]
        romanSet = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    digit = int(digit) - 1

    if digit == -1:
        pass
    else:
        roman = roman+romanSet[digit]

    return(roman)


def int_to_romanNumeral(number: int):
    if (number > 3999):
        return("err, number to high")
    else:
        roman = ""

        s_number = str(number)

        if (number > 999):  # thousand
            roman = romanNum(roman, 1000, s_number)

        if (number > 99):  # hundred
            roman = romanNum(roman, 100, s_number)

        if (number > 9):  # ten
            roman = romanNum(roman, 10, s_number)

        # one
        roman = romanNum(roman, 1, s_number)

        return(roman)


while True:
    now = datetime.now()
    print(f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}")
    print(f"{int_to_romanNumeral(now.year)}-{int_to_romanNumeral(now.month)}-{int_to_romanNumeral(now.day)} {int_to_romanNumeral(now.hour)}:{int_to_romanNumeral(now.minute)}:{int_to_romanNumeral(now.second)}")
    time.sleep(1)
    clear()
