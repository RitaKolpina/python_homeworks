from Address import Address
from Mailing import Mailing

to_address = Address
from_address = Address
to_address = 186420, "г. Сегежа", "ул. Бульвар Советов", 1, 33
from_address = 190000, "г. Санкт-Петурбург", "ул. Чернышевского", 40, 22

sending = Mailing
sending(to_address, from_address, 3000, 123456123)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)