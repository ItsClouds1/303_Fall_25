import string
import datetime

def encode(text, shift):
	letters_lower = string.ascii_lowercase
	text_encoded = text.lower().translate(str.maketrans(letters_lower, (letters_lower[shift % 26:] + letters_lower[:shift % 26])))
	return (list(letters_lower), text_encoded)

def decode(input_text, shift):
	letters_lower = string.ascii_lowercase
	text_decoded = input_text.lower().translate(str.maketrans(letters_lower, letters_lower[-shift % 26:] + letters_lower[:-shift % 26]))
	return text_decoded

class BankAccount():
	def __init__(self, name="Rainy", id="1234", creation_date=datetime.date.today(), balance=0):
		if creation_date > datetime.date.today(): raise Exception()
		self.name = name
		self.id = id
		self.creation_date = creation_date
		self.balance = balance
		return
	
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"New Balance: {self.balance}")
		return
	
	def withdraw(self, amount):
		self.balance -= amount
		print(f"New Balance: {self.balance}")
		return
	
	def view_balance(self):
		print(f"Current Balance: {self.balance}")
		return

class SavingsAccount(BankAccount): 
	def withdraw(self, amount):
		age = (datetime.date.today() - self.creation_date).days

		if age < 180:
			print("Account less than 180 days old")
			return
		if amount > self.balance:
			print("Insufficient funds")
			return
		
		self.balance -= amount
		print(f"New Savings Balance: {self.balance}")
		return

class CheckingAccount(BankAccount):
	def withdraw(self, amount):
		self.balance -= amount
		if self.balance < 0:
			self.balance -= 30
		print(f"New Checking Balance: {self.balance}")
		return