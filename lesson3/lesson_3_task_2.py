from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple", "13 mini", "+79990076545")
phone2 = Smartphone("Lenovo", "20", "+79990062212")
phone3 = Smartphone("Honor", "30i", "+79050062212")
phone4 = Smartphone("Samsung", "31S", "+79990555552")
phone5 = Smartphone("LG", "S12", "+79214216209")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")