class Customers:
    def __init__(self):
        self.name = None
        self.address = None
        self.phone = None
        self.balance = None

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        if len(phone) == 12:
            self.phone = phone
            return True
        else:
            print("Phone number needs to be ###-###-####")
            return False

    def set_balance(self, balance):
        if int(balance) > 0:
            self.balance = balance
            return True
        else:
            print("A negative balance is not allowed.")
            return False

    def print_customer(self):
        print(self.name, "at", self.address, "and the phone number", self.phone, "owes $", self.balance)


customers = list()
for i in range(0,6):
    temp = Customers()
    temp.set_name(input("Input the name of the person:"))
    temp.set_address(input("Input the address:"))
    while not temp.set_phone(input("Input the phone number:")):
        print("Please enter the phone number again:")
    while not temp.set_balance(input("Input the balance:")):
        print("Please enter the balance again:")
    customers.append(temp)
individual = input("Which customer do you want to list?")
for i in range(0, 6):
    if customers[i].name == individual:
        customers[i].print_customer()
