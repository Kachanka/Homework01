from adress import Address
from mailing import Mailling

to_adress = Address("620141", "Екатеринбург", "Пехотинцев", "12", "оф. 2-3")

from_adress = Address("620141", "Екатеринбург", "Автомагистральная", "15", "12")

mailing = Mailling(to_adress, from_adress, "5250", "1443686762")

