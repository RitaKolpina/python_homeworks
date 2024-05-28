from address import Address
from mailing import Mailing


to_address = Address("186420", "Сегежа", "Бульвар Советов", "1", "33")
from_address = Address ("190000", "Санкт-Петурбург", "Чернышевского", "40", "22")
mailing = Mailing(to_address, from_address, 3000, 123456123)

print(f"Send {mailing.track} from {mailing.from_address.index}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.home_number} - {mailing.from_address.flat_number} "
      f"to {mailing.to_address.index}, {mailing.from_address.city}, {mailing.to_address.street}, "
      f" {mailing.to_address.home_number} - {mailing.to_address.flat_number}. Cost {mailing.cost} rubles.")