class Dog:
    def __init__(self, name, breed = "Local"):      # Dunder method, initializer for a class
        self.name = name                            # Self passes the object itself 
        self.breed = breed

    def bark(self):                                 # Functions belonging to classes are called methods
        print("Bhow Bhow")
        print(f"My name is {self.name}")

# Inheritance

class germanShepherd(Dog):
    def __init__(self, name):
        self.breed = "German Shepherd"
        self.name = name

    def speak(self):
        print(f"My name is {self.name} and I am a German Shepherd")
        print("Ich komme aus Deutschland!")

class Bank:
    def __init__(self, balance):
        self._balance = balance             # use of private variable

    def checkBalance(self):
        print(f"Your current balance is rupees {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"Account credited with rupees {amount}")

    def withdraw(self, amount):
            self._balance -= amount
            print(f"Account debited with rupees {amount}")

    
dog1 = Dog("Jimmy")
dog1.bark()
dog2 = germanShepherd("Adolf")
dog2.speak()


acc1 = Bank(1000)
acc1.checkBalance()
acc1.withdraw(20)
acc1.deposit(1500)
acc1.checkBalance()

# Output

# Your current balance is rupees 1000
# Account debited with rupees 20
# Account credited with rupees 1500
# Your current balance is rupees 2480

# Python equivalent of private, public and protected are _var, var, __var (double underscore one is known as name mangling)
