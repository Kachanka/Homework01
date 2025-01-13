def is_yesr_leap(year):
    if (year % 4 == 0):
        print(f"Year: {year} - True")
    else:
        print(f"Year: {year} - False")


is_yesr_leap(int(input("Type a year: ")))
