class Account(object): 

	ID_COUNT = 1

	def __init__(self, name, **kwargs): 
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1
	
	def transfer(self, amount): 
		self.value += amount



class Bank(object):
	"""The bank"""

	def __init__(self):
		"""PAS TOUCHE A ICI MON 🐺"""
		self.account = []

	def add(self, account):
		self.account.append(account)

	def check_account(self, account):
		if not isinstance(account, (int, str)):
			print("The Object is not an account id or an account name.")
			return False
		if (all(account != number.id and account != number.name for number in self.account)):
			print("account doesn't exist")
			return False
		else:
			for number in self.account:
				if account == number.id or account == number.name:
					account = number

		if not hasattr(account, 'id'):
			return False
		if not hasattr(account, 'name'):
			return False
		if not hasattr(account, 'value'):
			return False

		b_list = [word for word in account.__dict__ if word[0] == 'b']
		if len(b_list) != 0:
			return False

		addr_list = [word for word in account.__dict__ if word[:3] == "zip" or word[:4] == "addr"]
		if len(addr_list) < 1:	
			return False

		if len(account.__dict__) % 2 == 0:
			return False
		return True


	def transfer(self, origin, dest, amount): 
		"""
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
		"""
		if not self.check_account(origin) or not self.check_account(dest):
			return False
		for index, elem in enumerate(self.account):
				if origin == elem.id or origin == elem.name:
					origin_index = index
				if dest == elem.id or dest == elem.name:
					dest_index = index
		if not isinstance(amount, float) or amount < 0:
			if not isinstance(amount, float):
				print("value is not a float")
			if amount <= 0:
				print("value must be greater or equal to 0")
			return False
		elif self.account[origin_index].value < amount:
			print("Fonds Insuffisants")
			return False
		else:
			self.account[origin_index].value -= amount
			self.account[dest_index].value += amount
			return True
	
	def fix_account(self, account):
		"""
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
		"""

		if not isinstance(account, (int, str)):
			print("The Object is not an account id or an account name.")
			return False
		if (all(account != number.id and account != number.name for number in self.account)):
			print("account doesn't exist")
			return False
		else:
			for number in self.account:
				if account == number.id or account == number.name:
					account = number
		if not hasattr(account, 'id'):
			account.id = account.ID_COUNT
		if not hasattr(account, 'name'):
			account.name = "random name"
		if not hasattr(account, 'value'):
			account.value = 0

		b_list = [word for word in account.__dict__ if word[0] == 'b']
		for word in b_list:
			account.__dict__['z' + word[1:]] = account.__dict__[word]
			delattr(account, word)

		addr_list = [word for word in account.__dict__ if word[:3] == "zip" or word[:4] == "addr"]
		if len(addr_list) == 0:
			account.__dict__["zip"] = "Random-Zip"

		if len(account.__dict__) % 2 == 0:
			account.__dict__["odd"] = "So it can be odd."
		return True



#ac1 = Account("Jean Eudes", Taille='1.81')
#ac2 = Account("Marie-C")
#bk = Bank()
#bk.add(ac1)
#bk.fix_account(1)
#print(ac1.__dict__)