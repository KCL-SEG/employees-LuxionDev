"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    total_pay = 0
    hours = 0
    comsission = 0
    contracts = 0
    
    def __init__(self, name, contract_type, pay):
        self.name = name
        self.pay = pay
        
        if "salary" in contract_type.lower():
            self.contract_type = "salary"
        else:
            self.contract_type = "hourly"
        
    def set_hours(self, hours):
        self.hours = hours

    def set_commission(self, comission, contracts=1,):
        self.comsission = comission
        self.contracts = contracts

    def get_pay(self):
        total = self.pay
        if self.contract_type == "hourly":
            total *= self.hours
        if self.comsission > 0:
            total += (self.comsission * self.contracts)

        return total

    def __str__(self):
        string = self.name + " works on a "
        
        if self.contract_type == "salary":
            string += "monthly salary of " + str(self.pay)
        else:
            string += "contract of " + str(self.hours) + " hours at " + str(self.pay) + "/hour"

        if self.comsission > 0:
            string += " and receives a "
            
            if self.contracts > 1:
                string += "commission for " + str(self.contracts) + " contract(s) at " + str(self.comsission) + "/contract."
            else:
                string += "bonus commission of " + str(self.comsission) + "."

        else:
            string += "."

        string += " Their total pay is " + str(self.get_pay()) + "."

        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "salary", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 25)
charlie.set_hours(100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "salary", 3000)
renee.set_commission(200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 25)
jan.set_hours(150)
jan.set_commission(220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "salary", 2000)
robbie.set_commission(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 30)
ariel.set_hours(120)
ariel.set_commission(600)