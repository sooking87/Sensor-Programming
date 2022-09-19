def validate(str):
    if (str in '.'):
        year, month, day = str.split(".")
    elif (str in "-"):
        year, month, day = str.split("-")
    elif (str in " "):
        year, month, day = str.split()

    year = int(year)
    month = int(month)
    day = int(day)

    return year, month, day


y, m, d = validate("2022-08-07")

print(y)
