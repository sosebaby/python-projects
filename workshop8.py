#1
inventory = {'apples': 50,
            'bananas': 120,
            'oranges': 80,
            'grapes': 45,
            'pears': 60}
total = sum(inventory.values())#selects the values only
average = sum(inventory.values()) / len(inventory.values())
sumproductlength = sum(len(i) for i in inventory.keys())
averageofproductlength = sumproductlength / len(inventory.keys())

print(f"The total of the items are: {total}")
print(f"Average items per product: {average}")
print(f"Sum of product name lengths: {sumproductlength}")
print(f"Average product name length: {averageofproductlength}")

#3
class Orders:
    def __init__(self):
        self.listoforders = {
            'apples': [6, 10, 8],
            'bananas': [9, 17, 4, 2],
            'oranges': [9, 5],
            'grapes': [2, 7, 3, 9]
        }
    def inputorders(self):
            names = input("Enter your name: ")
            print(f"Hi! {names}")
            noitems = int(input("How many items do you want to order? "))
            for no in range (noitems):
                nameofitem = input("Enter item name: ")
                quantityofitem = int(input("What is the quantity of the item? "))
                if nameofitem in self.listoforders:
                    self.listoforders[nameofitem].append(quantityofitem)
                else:
                        self.listoforders[nameofitem] = [quantityofitem]
            self.calculateorderstats()
    def makeorderdict(self):
        return self.listoforders
    def calculateorderstats(self):
        allquantities = [quantity for quantities in self.listoforders.values() for quantity in quantities]
        total = sum(allquantities)
        average = total / len(allquantities) if allquantities else 0
        print(f"Total ordered items: {total}")
        print(f"Average quantity per item: {average}")

#2
class Countries:
    def __init__(self):
        self.countriesandcapitals = {'Canada': 'Ottawa',
                             'France': 'Paris',
                             'Japan': 'Tokyo',
                             'India': 'New Delhi',
                             'Brazil': 'Brasilia'}
    def getcapital(self):
        while True:
            scene1 = input("Would you like to (R)etrieve a capital, (A)dd a country, or (Q)uit?")
            if scene1 == "R":
                countrytoretrieve = input("Enter the country name: ")
                if countrytoretrieve in self.countriesandcapitals:
                    print(f"The capital of {countrytoretrieve} is {self.countriesandcapitals.get(countrytoretrieve)}")
                else:
                    print(f"The capital of {countrytoretrieve} is:", "Country does not exist")
            elif scene1 == "A":
                            self.addcountry()            
            elif scene1 == "Q":
                print("Thank you for stopping by!!")
                break
            else:
                print("Invalid input. Please enter 'R', 'A', or 'Q'.")
    def addcountry(self):
        newcountry = input("Enter the name of the country you would like to add: ")
        if newcountry in self.countriesandcapitals:
            print(f"{newcountry} already exists in the list of countries, please retrieve it or add a new country")
        else:
            newcapital = input(f"Enter the capital of {newcountry}: ")
            self.countriesandcapitals[newcountry] = newcapital
            print(f"{newcountry} with the capital {newcapital} has been added to the list")    
def main():
    orders = Orders()
    orders.inputorders()    
    countries = Countries()
    countries.getcapital()
if __name__ == "__main__":
    main()
    
