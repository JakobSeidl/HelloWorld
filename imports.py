myString = 'imports'

print('We have been importing %s' % myString)


class CreditCard:
    def __init__(self, cardNumber):
        self.cardNumber = cardNumber
        self.validity = False

    def getSecondDigits(self):
        print('%s' % str(self.cardNumber))
