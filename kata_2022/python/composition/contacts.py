class Address:
    def __init__(self, street, street2, city, state, zipcode):
        self.street = street
        self.street2 = street2

        self.city = city

        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state} {self.zipcode}")
        return "\n".join(lines)