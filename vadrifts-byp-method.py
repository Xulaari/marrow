import pyperclip
# UNICODE IS ⁥

method = input("select method: ")

unicode = "⁥⁥⁥⁥"

if method == "1":
    tab = {
        "a": "а",
        "c": "с",
        "e": "е",
        "j": "ј",
        "l": "ӏ",
        "s": "ѕ",
        "h": "һ",
        "v": "ν",
        "o": "о",
        "p": "р",
        "x": "х",
        "y": "у",
        "A": "Α",
        "B": "Β",
        "C": "С",
        "E": "Е",
        "N": "Ν",
        "I": "І",
        "M": "М",
        "O": "О",
        "H": "Н",
        "J": "Ј",
        "K": "Κ",
        "M": "Μ",
        "N": "Ν",
        "S": "Ѕ",
        "T": "Τ",
        "P": "Р",
        "X": "Χ",
        "Y": "Υ",
        "Z": "Ζ"
    }
else:
    tab = {
        "a": "а" + "𐌑𝖔 ͜ ͣ ",
        "c": "с" + "𐌑𝖔 ͜ ͣ ",
        "e": "е" + "𐌑𝖔 ͜ ͣ ",
        "j": "ј" + "𐌑𝖔 ͜ ͣ ",
        "l": "ӏ" + "𐌑𝖔 ͜ ͣ ",
        "h": "һ" + "𐌑𝖔 ͜ ͣ ",
        "i": "і" + "𐌑𝖔 ͜ ͣ ",
        "v": "ν" + "𐌑𝖔 ͜ ͣ ",
        "o": "о" + "𐌑𝖔 ͜ ͣ ",
        "p": "р" + "𐌑𝖔 ͜ ͣ ",
        "x": "х" + "𐌑𝖔 ͜ ͣ ",
        "y": "у" + "𐌑𝖔 ͜ ͣ ",
        "s": "ѕ" + "𐌑𝖔 ͜ ͣ ",
        "A": "Α" + "𐌑𝖔 ͜ ͣ ",
        "B": "Β" + "𐌑𝖔 ͜ ͣ ",
        "C": "С" + "𐌑𝖔 ͜ ͣ ",
        "E": "Е" + "𐌑𝖔 ͜ ͣ ",
        "N": "Ν" + "𐌑𝖔 ͜ ͣ ",
        "I": "І" + "𐌑𝖔 ͜ ͣ ",
        "M": "М" + "𐌑𝖔 ͜ ͣ ",
        "O": "О" + "𐌑𝖔 ͜ ͣ ",
        "H": "Н" + "𐌑𝖔 ͜ ͣ ",
        "J": "Ј" + "𐌑𝖔 ͜ ͣ ",
        "K": "Κ" + "𐌑𝖔 ͜ ͣ ",
        "M": "Μ" + "𐌑𝖔 ͜ ͣ ",
        "N": "Ν" + "𐌑𝖔 ͜ ͣ ",
        "S": "Ѕ" + "𐌑𝖔 ͜ ͣ ",
        "T": "Τ" + "𐌑𝖔 ͜ ͣ ",
        "P": "Р" + "𐌑𝖔 ͜ ͣ ",
        "X": "Χ" + "𐌑𝖔 ͜ ͣ ",
        "Y": "Υ" + "𐌑𝖔 ͜ ͣ ",
        "Z": "Ζ" + "𐌑𝖔 ͜ ͣ ",
        " ": "  ",
    }

while True:
    string = list(input("enter to conv: "))

    convertedstring = ""

    for char in string:
        convertedchar = tab.get(char, char)
        convertedstring += convertedchar

    if method == "1":
        endr = unicode + unicode.join(convertedstring)
    else:
        endr = "".join(convertedstring)

    print(endr)

    pyperclip.copy(endr)
