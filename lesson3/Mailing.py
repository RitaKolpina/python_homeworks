from Address import Address


class Mailing:
    to_address = Address
    from_address = Address
    cost = "3000"
    track = "123456123"

    def __init__(self, to_address, from_address, cost, track):
        self.t = to_address
        self.f = from_address
        self.c = cost
        self.t = track

    def to_address(self):
        print(self.to_address)

    def from_address(self):
        print(self.from_address)