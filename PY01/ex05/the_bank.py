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
		self.fix_account(account)
		self.account.append(account)

	def transfer(self, origin, dest, amount): 
		"""
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
		"""
	
	
	def fix_account(self, account):
		"""
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
		"""

		if not isinstance(account, Account):
			raise ValueError("The Object is not an account.")
		if not hasattr(account, 'id'):
			account.id = account.ID_COUNT
		if not hasattr(account, 'name'):
			account.name = "random name"
		if not hasattr(account, 'value'):
			account.id = 0

		b_list = [word for word in account.__dict__ if word[0] == 'b']
		for word in b_list:
			account.__dict__['z' + word[1:]] = account.__dict__[word]
			delattr(account, word)

		addr_list = [word for word in account.__dict__ if word[:3] == "zip" or word[:4] == "addr"]
		if len(addr_list) == 0:
			account.__dict__["zip"] = "Random-Zip"

		if sum(i for i, x in enumerate(account.__dict__)) % 2 == 0:
			account.__dict__["odd"] = "So it can be odd."



ac1 = Account("Jean Eudes")
bk = Bank()
bk.fix_account(ac1)
print(ac1.__dict__)