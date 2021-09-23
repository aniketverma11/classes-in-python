class WizCoin:

    def __init__(self, galleons, sickles, knuts):
        """Create a new wizcoin object with galleons sickles and knuts"""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def values(self):
        """The values(in knuts) of all the coins in this wizcoin object"""
        return (self.galleons*17*29) + (self.sickles*29) + (self.knuts)

    def weightInGrams(self):
        """Return the weight of the coin in grams"""
        return (self.galleons*31.103)+(self.sickles*11.34)+(self.knuts*5.0)


a = WizCoin(9,5,6)
print(a.values())
