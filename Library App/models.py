from app import db
from app import app
'''from hashlib import md5

import sys
if sys.version_info >= (3,0):
	enable_search = False

else:
	enable_search = True
	import flask.ext.whooshalchemy as whooshalchemy
'''

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	department = db.Column(db.String(100))
	studnum  = db.Column(db.String(100))
	email  = db.Column(db.String(100))
	telnum  = db.Column(db.String(100))
	address  = db.Column(db.String(100))
	username  = db.Column(db.String(100), index = True, unique=True)
	password  = db.Column(db.String(100))
	
		
	def __init__(self,firstname,lastname,department,studnum,email,telnum,address,username,password):
		self.firstname = firstname
		self.lastname = lastname
		self.department = department
		self.studnum = studnum
		self.email = email
		self.telnum = telnum
		self.address = address
		self.username = username
		self.password = password

	'''		
	def get_id(self):
		try:
			return unicode(self.id)
		except NameError:
			return str(self.id)
'''
	def user_books(self):
		return Loan.query.filter(id > 0)

	def __repr__(self):
		return '<Users %r>' %(self.username)



class Book(db.Model):
	__searchable__ = ['title']
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	author = db.Column(db.String(100))
	subject = db.Column(db.String(100))
	section  = db.Column(db.String(100))
	publisher  = db.Column(db.String(100))
	pubyear  = db.Column(db.String(100))
	isavailable  = db.Column(db.String(100))
	isloaned  = db.Column(db.String(100))
	isreturned  = db.Column(db.String(100))
		
	def __init__(self,title,author,subject,section,publisher,pubyear,isavailable,isloaned,isreturned):
		self.title = title
		self.author = author
		self.subject = subject
		self.section = section
		self.publisher = publisher
		self.pubyear = pubyear
		self.isavailable = isavailable
		self.isloaned = isloaned
		self.isreturned = isreturned

 

	def __repr__(self):
		return '<Book %r>' %(self.title)


class Author(db.Model):
	__authorsearch__ = ['name']
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	bookid = db.Column(db.String(100), db.ForeignKey('book.id'))

	def __init__(self,firstname,lastname,bookid):
		self.firstname = firstname
		self.lastname = lastname
		self.bookid = bookid


class Loan(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	bookid = db.Column(db.String(100), db.ForeignKey('book.id'))
	userid = db.Column(db.String(100), db.ForeignKey('user.id'))
	
		
	def __init__(self,bookid,userid):
		self.bookid = bookid
		self.userid = userid
		
	def __repr__(self):
		return '<Loan %r %r>' %(self.bookid, self.userid)

class Rturned(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	bookid = db.Column(db.String(100), db.ForeignKey('book.id'))
	userid = db.Column(db.String(100), db.ForeignKey('user.id'))
	
		
	def __init__(self,bookid,userid):
		self.bookid = bookid
		self.userid = userid
	
	def __repr__(self):
		return '<Rturned %r %r>' % (self.bookid, self.userid)

	