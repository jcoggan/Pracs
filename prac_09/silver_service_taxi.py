from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip + flagfall"""
        return self.flagfall + super().get_fare()

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"
