#The solutions follow python2

#3.5.1 
"""
class Temperature(object):
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9.0/5.0) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5.0/9.0

# Example usage
print "25°C to Fahrenheit:", Temperature.celsius_to_fahrenheit(25)  # Output: 77.0
print "77°F to Celsius:", Temperature.fahrenheit_to_celsius(77)  # Output: 25.0

"""

#3.5.2

"""
class Payment(object):
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return "Processing credit card payment of $%s" % amount

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return "Processing PayPal payment of $%s" % amount

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        return "Processing Bitcoin payment of $%s" % amount

def process_payment(payment_method, amount):
    print payment_method.process_payment(amount)

# Example usage
credit_card = CreditCardPayment()
paypal = PayPalPayment()
bitcoin = BitcoinPayment()

process_payment(credit_card, 100)  # Output: Processing credit card payment of $100
process_payment(paypal, 150)       # Output: Processing PayPal payment of $150
process_payment(bitcoin, 200)      # Output: Processing Bitcoin payment of $200

"""

#3.5.3 
"""
class FlyingAnimal(object):
    def fly(self):
        return "This animal can fly"

class SwimmingAnimal(object):
    def swim(self):
        return "This animal can swim"

class Duck(FlyingAnimal, SwimmingAnimal):
    def quack(self):
        return "Quack quack!"

# Example usage
donald = Duck()
print donald.fly()  # Output: This animal can fly
print donald.swim()  # Output: This animal can swim
print donald.quack()  # Output: Quack quack!

"""
