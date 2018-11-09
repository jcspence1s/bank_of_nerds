from getpass import getpass
import hashlib


class Account:
    def __init__(self, account_num):
        self.account_id = account_num
        self.balance = 0
        self.withdrawls = 0
        self.deposits = 0
        self.interest = 0

    def withdraw(self, amount):
        if amount < 0:
            print("Can't withdraw negative monies.")
            return
        withdrawn = self.balance - amount
        if withdrawn < 0:
            print("You will incur over draft fees of 35$.")
            withdrawn -= 35
            self.balance = withdrawn
        else:
            self.balance = withdrawn
            self.withdrawls += 1

    def deposit(self, amount):
        if amount < 0:
            print("Can't deposit negative monies.")
            return
        self.balance += amount
        self.deposits += 1

    def __str__(self, type_of_account):
        acc_string = "{0} account: {1} \n   Balance: ${2:.2f}".format(
                     type_of_account, self.account_id, self.balance)
        return acc_string


class Checking(Account):
    checking_id = 10000000

    def __init__(self):
        super().__init__(Checking.checking_id)
        print("Checking", Checking.checking_id)
        Checking.checking_id += 1

    def __str__(self):
        return super().__str__("Checking")


class Savings(Account):
    savings_id = 10000000

    def __init__(self):
        super().__init__(Savings.savings_id)
        print("Savings", Savings.savings_id)
        Savings.savings_id += 1
        self.interest = 0.05

    def __str__(self):
        return super().__str__("Savings")


class FourOhOneK(Account):
    four_oh_one_k_id = 10000000

    def __init__(self):
        super().__init__(FourOhOneK.four_oh_one_k_id)
        FourOhOneK.four_oh_one_k_id += 1
        self.interest = 0.05

    def __str__(self):
        return super().__str__("401k")


class Customer:
    customer_id = 1000
    customers = dict()

    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.id = Customer.customer_id
        self.accounts = {'Checking': {}, 'Savings': {}, '401k': {}}
        if username in Customer.customers:
            print("Username taken.")
            return None
        self.password = self.get_password()
        Customer.customers.update({username: self})
        Customer.customer_id += 1

    def get_password(self):
        pw_prompt = "Please enter a password.\n>"
        pw_confirm = "Please confirm your password.\n>"
        while True:
            try:
                first_attempt = getpass(pw_prompt)
                confirmation = getpass(pw_confirm)
                if not first_attempt or not confirmation:
                    print("Password cannot be empty.")
                elif first_attempt == confirmation:
                    digest = hashlib.md5(
                            confirmation.encode("utf-8")).hexdigest()
                    return digest
                else:
                    print("Passwords do not match. Try Again.")
            except (KeyboardInterrupt, EOFError):
                # Passing silently to not allow account without password
                pass

    def __str__(self):
        output = "Name: {} {}\nAge: {}\nId: {}"
        return output.format(
                self.first_name, self.last_name, self.age, self.id)
