'''import sqlite3

with sqlite3.connect("user.db") as connection:
	c = connection.cursor()

	c.execute("DROP TABLE users")
	c.execute("CREATE TABLE users(ID INT, firstname TEXT, lastname TEXT, department TEXT, studnum TEXT, email TEXT, telnum TEXT, address TEXT, username TEXT, password TEXT, table TEXT)")

	c.commit()

with sqlite3.connect("user.db") as connection:
	x = connection.cursor()

	x.execute("DROP TABLE books")
	x.execute("CREATE TABLE books(ID INT, title TEXT, author TEXT, subject TEXT, section TEXT, publisher TEXT, pubyear TEXT, isavailable TEXT, isloaned TEXT, isreturned TEXT, table TEXT)")
	x.commit()

	x.execute("DROP TABLE loan")
	x.execute("CREATE TABLE loan(ID INT, bookid TEXT, userid TEXT, table TEXT)")
	x.commit()

	x.execute("DROP TABLE rturned")
	x.execute("CREATE TABLE rturned(ID INT, bookid TEXT, userid TEXT, table TEXT)")
	x.commit()
	'''