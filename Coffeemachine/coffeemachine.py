class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    cash = 550
    disposable_cups = 9
    counter = 0
    status = "wait"

    def action(self, command):
        if command == "buy":
            self.status = "make"
        elif command == "fill":
            self.status = "fill"
            self.counter = 0
        elif command == "take":
            print(f"I gave you {self.cash}")
            self.cash = 0
        elif command == "remaining":
            print("The coffee machine has:")
            print(f"{self.water} of water\n {self.milk} of milk\n{self.coffee_beans} of coffee\n "
                  f"{self.disposable_cups} of disposable cups\n {self.cash} of money")

        elif self.status == "make":
            if type == 4:
                self.status = "wait"
                return
            # for espresso
            if type == 1:
                self.m_coffee(4, 250, 16)
            # for latte
            elif type == 2:
                self.m_coffee(7, 350, 20, 75)
            # for cappuccino
            elif type == 3:
                self.m_coffee(6, 200, 10, 100)
            self.status = "wait"
        elif self.status == "fill":
            v = int(command)
            if self.counter == 0:
                self.water += v
            elif self.counter == 1:
                self.coffee_beans += v
            elif self.counter == 2:
                self.milk += v
            elif self.counter == 3:
                self.disposable_cups += v
            elif self.counter == 4:
                self.cash += v
                self.status = "wait"
                self.counter = -1
            self.counter += 1
        else:
            self.status = "wait"

    def m_coffee(self, take_cash, n_water, n_coffee, n_milk=0):
        if self.water < n_water:
            print("Sorry, not enough water!")
        elif self.coffee_beans < n_coffee:
            print("Sorry, not enough coffee!")
        elif self.milk < n_milk:
            print("Sorry, not enough milk!")

        else:
            print("I have enough resources, making you a coffee!")
            self.water -= n_water
            self.coffee_beans -= n_coffee
            self.milk -= n_milk
            self.disposable_cups -= 1
            self.cash += take_cash


coffee_machine = CoffeeMachine()
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n>")
    coffee_machine.action(action)
    if action == "buy":
        type_of_coffee = input("What do you want to buy?  1- espresso, 2 - latte, 3 - cappuccino , 4 - back for menu "
                               ":\n>")
        coffee_machine.action(type_of_coffee)
    elif action == "fill":
        water = input("Write how many ml of water you want to add:\n>")
        coffee_machine.action(water)
        milk = input("Write how many ml of milk you want to add:\n>")
        coffee_machine.action(milk)
        coffee = input("Write how many grams of coffee beans you want to add:\n>")
        coffee_machine.action(coffee)
        cups = input("Write how many disposable coffee cups you want to add:\n>")
        coffee_machine.action(cups)
        grn = input("Write how many money you want to add:\n>")
        coffee_machine.action(grn)
    elif action == "exit":
        break
