
def month_to_season(month):

    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Номера месяца не существует"


if __name__ == "__main__":
    month = int(input("Введите номер месяца (1-12): "))
    season = month_to_season(month)
    print(f"Месяц {month} относится к сезону {season}")
