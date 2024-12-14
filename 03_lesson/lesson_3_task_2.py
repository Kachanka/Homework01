from smartphone import Smartphone

catalog = []
phone1 = Smartphone("TECNO", "POVA 6", "+79921457892")
phone2 = Smartphone("POCO", "F7", "+79992563432")
phone3 = Smartphone("Xiaomi", "15 Pro", "+79876548932")
phone4 = Smartphone("Samsung", "Galaxy S24", "+79962589674")
phone5 = Smartphone("Google", "Pixel 8 Pro", "+79526348519")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. - {phone.phone_number}")