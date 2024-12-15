from adress import Address
from mailing import Mailing

to_adress = Address("620141", "Екатеринбург", "Пехотинцев", "12", "оф. 2-3")

from_adress = Address("620141", "Екатеринбург", "Автомагистральная", "15", "12")

mailing = Mailing(to_adress, from_adress, "5250", "1443686762")

