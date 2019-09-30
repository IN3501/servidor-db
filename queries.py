import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('database.db')
c = conn.cursor()

while(True):
	print("Inserte una query")
	try:
		query = input()
		ans = c.execute(query)
		descriptions = []
		for value in ans.description:
			descriptions.append(value[0])
		print(tabulate(ans.fetchall(), headers=descriptions))
	except Exception as e:
		print("----------")
		print("Error:")
		print(e)
		print("----------")